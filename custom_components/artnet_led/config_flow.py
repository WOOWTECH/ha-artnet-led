"""Config flow for Art-Net LED integration."""
from __future__ import annotations

import ipaddress
import logging
import uuid
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN,
    # Node types
    NODE_TYPES,
    NODE_TYPE_ARTNET_DIRECT,
    NODE_TYPE_LABELS,
    DEFAULT_PORTS,
    # Light types
    LIGHT_TYPES,
    LIGHT_TYPE_DIMMER,
    LIGHT_TYPE_LABELS,
    LIGHT_TYPE_COLOR_TEMP,
    LIGHT_TYPE_RGB,
    LIGHT_TYPE_RGBW,
    LIGHT_TYPE_RGBWW,
    LIGHT_TYPE_XY,
    LIGHT_TYPE_FIXED,
    CHANNEL_COUNTS,
    DEFAULT_CHANNEL_SETUPS,
    # Output corrections
    OUTPUT_CORRECTIONS,
    OUTPUT_CORRECTION_LABELS,
    # Channel sizes and byte orders
    CHANNEL_SIZES,
    CHANNEL_SIZE_LABELS,
    BYTE_ORDERS,
    BYTE_ORDER_LABELS,
    CHANNEL_SETUP_CODES,
    # Config keys
    CONF_HOST,
    CONF_PORT,
    CONF_NODE_TYPE,
    CONF_MAX_FPS,
    CONF_REFRESH_EVERY,
    CONF_HOST_OVERRIDE,
    CONF_PORT_OVERRIDE,
    CONF_UNIVERSES,
    CONF_UNIVERSE_NUMBER,
    CONF_OUTPUT_CORRECTION,
    CONF_SEND_PARTIAL_UNIVERSE,
    CONF_DEVICES,
    CONF_FIXTURE_ID,
    CONF_CHANNEL,
    CONF_NAME,
    CONF_TYPE,
    CONF_TRANSITION,
    CONF_CHANNEL_SIZE,
    CONF_BYTE_ORDER,
    CONF_CHANNEL_SETUP,
    CONF_CHANNEL_COUNT,
    CONF_MIN_TEMP,
    CONF_MAX_TEMP,
    # Defaults
    DEFAULT_MAX_FPS,
    DEFAULT_REFRESH_EVERY,
    DEFAULT_TRANSITION,
    DEFAULT_OUTPUT_CORRECTION,
    DEFAULT_CHANNEL_SIZE,
    DEFAULT_BYTE_ORDER,
    DEFAULT_SEND_PARTIAL_UNIVERSE,
    DEFAULT_MIN_TEMP,
    DEFAULT_MAX_TEMP,
    DEFAULT_CHANNEL_COUNT,
    # Limits
    MIN_UNIVERSE,
    MAX_UNIVERSE,
    MIN_CHANNEL,
    MAX_CHANNEL,
    MIN_FPS,
    MAX_FPS,
    MIN_REFRESH,
    MAX_REFRESH,
    MIN_PORT,
    MAX_PORT,
    MIN_TRANSITION,
    MAX_TRANSITION,
    MAX_FIXED_CHANNELS,
)

_LOGGER = logging.getLogger(__name__)


class ArtNetLedConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Art-Net LED."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self._connection_data: dict[str, Any] = {}
        self._universes: dict[str, dict[str, Any]] = {}
        self._fixtures: list[dict[str, Any]] = []
        self._pending_fixture: dict[str, Any] = {}
        self._temp_entities: list[str] = []

    # ─────────────────────────────────────────────────────────────────
    # STEP 1: CONNECTION
    # ─────────────────────────────────────────────────────────────────
    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the connection configuration step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            errors = self._validate_connection(user_input)
            if not errors:
                self._connection_data = user_input
                return await self.async_step_universe()

        return self.async_show_form(
            step_id="user",
            data_schema=self._get_connection_schema(),
            errors=errors,
        )

    def _get_connection_schema(self) -> vol.Schema:
        """Get schema for connection step."""
        return vol.Schema(
            {
                vol.Required(CONF_HOST): str,
                vol.Required(
                    CONF_NODE_TYPE, default=NODE_TYPE_ARTNET_DIRECT
                ): vol.In({k: NODE_TYPE_LABELS[k] for k in NODE_TYPES}),
                vol.Optional(CONF_PORT): vol.Coerce(int),
                vol.Optional(CONF_MAX_FPS, default=DEFAULT_MAX_FPS): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_FPS, max=MAX_FPS)
                ),
                vol.Optional(
                    CONF_REFRESH_EVERY, default=DEFAULT_REFRESH_EVERY
                ): vol.All(
                    vol.Coerce(float), vol.Range(min=MIN_REFRESH, max=MAX_REFRESH)
                ),
                vol.Optional(CONF_HOST_OVERRIDE): str,
                vol.Optional(CONF_PORT_OVERRIDE): vol.Coerce(int),
            }
        )

    def _validate_connection(self, data: dict[str, Any]) -> dict[str, str]:
        """Validate connection settings."""
        errors: dict[str, str] = {}

        # IPv4 validation
        host = data.get(CONF_HOST, "")
        if not self._is_valid_ipv4(host):
            errors[CONF_HOST] = "invalid_host"

        # Port validation (if provided)
        port = data.get(CONF_PORT)
        if port is not None and not (MIN_PORT <= port <= MAX_PORT):
            errors[CONF_PORT] = "invalid_port"

        # Port override validation (if provided)
        port_override = data.get(CONF_PORT_OVERRIDE)
        if port_override is not None and not (MIN_PORT <= port_override <= MAX_PORT):
            errors[CONF_PORT_OVERRIDE] = "invalid_port"

        # Host override validation (if provided)
        host_override = data.get(CONF_HOST_OVERRIDE)
        if host_override and not self._is_valid_ipv4(host_override):
            errors[CONF_HOST_OVERRIDE] = "invalid_host"

        return errors

    @staticmethod
    def _is_valid_ipv4(ip: str) -> bool:
        """Validate IPv4 address format."""
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False

    # ─────────────────────────────────────────────────────────────────
    # STEP 2: UNIVERSE
    # ─────────────────────────────────────────────────────────────────
    async def async_step_universe(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle universe configuration step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            action = user_input.pop("action", "add")

            if action == "skip":
                # Skip to fixture step
                if not self._universes:
                    # Auto-create universe 1 if none added
                    self._universes["1"] = {
                        CONF_OUTPUT_CORRECTION: DEFAULT_OUTPUT_CORRECTION,
                        CONF_SEND_PARTIAL_UNIVERSE: DEFAULT_SEND_PARTIAL_UNIVERSE,
                        CONF_DEVICES: [],
                    }
                return await self.async_step_fixture()

            # Validate universe
            errors = self._validate_universe(user_input)
            if not errors:
                universe_num = str(user_input[CONF_UNIVERSE_NUMBER])
                self._universes[universe_num] = {
                    CONF_OUTPUT_CORRECTION: user_input.get(
                        CONF_OUTPUT_CORRECTION, DEFAULT_OUTPUT_CORRECTION
                    ),
                    CONF_SEND_PARTIAL_UNIVERSE: user_input.get(
                        CONF_SEND_PARTIAL_UNIVERSE, DEFAULT_SEND_PARTIAL_UNIVERSE
                    ),
                    CONF_DEVICES: [],
                }
                # Show form again for adding more universes
                return self.async_show_form(
                    step_id="universe",
                    data_schema=self._get_universe_schema(),
                    errors={},
                    description_placeholders={
                        "universes_added": ", ".join(sorted(self._universes.keys()))
                    },
                )

        return self.async_show_form(
            step_id="universe",
            data_schema=self._get_universe_schema(),
            errors=errors,
            description_placeholders={
                "universes_added": ", ".join(sorted(self._universes.keys()))
                if self._universes
                else "None"
            },
        )

    def _get_universe_schema(self) -> vol.Schema:
        """Get schema for universe step."""
        return vol.Schema(
            {
                vol.Required(CONF_UNIVERSE_NUMBER, default=1): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_UNIVERSE, max=MAX_UNIVERSE)
                ),
                vol.Optional(
                    CONF_OUTPUT_CORRECTION, default=DEFAULT_OUTPUT_CORRECTION
                ): vol.In({k: OUTPUT_CORRECTION_LABELS[k] for k in OUTPUT_CORRECTIONS}),
                vol.Optional(
                    CONF_SEND_PARTIAL_UNIVERSE, default=DEFAULT_SEND_PARTIAL_UNIVERSE
                ): bool,
                vol.Required("action", default="add"): vol.In(
                    {"add": "Add Universe", "skip": "Continue to Fixtures"}
                ),
            }
        )

    def _validate_universe(self, data: dict[str, Any]) -> dict[str, str]:
        """Validate universe settings."""
        errors: dict[str, str] = {}

        universe = data.get(CONF_UNIVERSE_NUMBER)
        if universe is None:
            errors[CONF_UNIVERSE_NUMBER] = "invalid_universe"
        elif not (MIN_UNIVERSE <= universe <= MAX_UNIVERSE):
            errors[CONF_UNIVERSE_NUMBER] = "invalid_universe"
        elif str(universe) in self._universes:
            errors[CONF_UNIVERSE_NUMBER] = "duplicate_universe"

        return errors

    # ─────────────────────────────────────────────────────────────────
    # STEP 3: FIXTURE (LOOP)
    # ─────────────────────────────────────────────────────────────────
    async def async_step_fixture(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle fixture configuration step (loops for multiple fixtures)."""
        errors: dict[str, str] = {}

        if user_input is not None:
            action = user_input.pop("action", "add")

            if action == "done":
                if not self._fixtures:
                    errors["base"] = "no_fixtures"
                else:
                    return await self.async_step_review()

            elif action == "add":
                # Validate basic fixture info
                errors = self._validate_fixture_basic(user_input)
                if not errors:
                    # Store pending fixture data
                    self._pending_fixture = dict(user_input)
                    fixture_type = user_input.get(CONF_TYPE, LIGHT_TYPE_DIMMER)

                    # Check if this type needs additional configuration
                    if self._type_needs_details(fixture_type):
                        return await self.async_step_fixture_details()
                    else:
                        # Add fixture directly (no extra fields needed)
                        return self._add_pending_fixture()

        return self.async_show_form(
            step_id="fixture",
            data_schema=self._get_fixture_schema(),
            errors=errors,
            description_placeholders={"fixtures_added": str(len(self._fixtures))},
        )

    def _type_needs_details(self, fixture_type: str) -> bool:
        """Check if fixture type needs additional detail fields."""
        # ALL types can have channel_setup for advanced users
        # Show details step for all types to allow channel_setup configuration
        return True

    async def async_step_fixture_details(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle type-specific fixture details."""
        errors: dict[str, str] = {}
        fixture_type = self._pending_fixture.get(CONF_TYPE, LIGHT_TYPE_DIMMER)

        if user_input is not None:
            # Validate type-specific fields
            errors = self._validate_fixture_details(user_input, fixture_type)
            if not errors:
                # Merge detail fields into pending fixture
                self._pending_fixture.update(user_input)
                return self._add_pending_fixture()

        return self.async_show_form(
            step_id="fixture_details",
            data_schema=self._get_fixture_details_schema(fixture_type),
            errors=errors,
            description_placeholders={
                "fixture_name": self._pending_fixture.get(CONF_NAME, "Fixture"),
                "fixture_type": LIGHT_TYPE_LABELS.get(fixture_type, fixture_type),
            },
        )

    def _add_pending_fixture(self) -> FlowResult:
        """Add the pending fixture and return to fixture step."""
        fixture_data = self._pending_fixture
        fixture_data[CONF_FIXTURE_ID] = str(uuid.uuid4())

        # Build channel_setup from type if not provided
        channel_setup = self._build_channel_setup(fixture_data)
        if channel_setup:
            fixture_data[CONF_CHANNEL_SETUP] = channel_setup

        self._fixtures.append(fixture_data)
        self._pending_fixture = {}
        _LOGGER.debug("Added fixture: %s", fixture_data)

        # Show empty form for next fixture
        return self.async_show_form(
            step_id="fixture",
            data_schema=self._get_fixture_schema(),
            errors={},
            description_placeholders={
                "fixtures_added": str(len(self._fixtures))
            },
        )

    def _get_fixture_schema(self) -> vol.Schema:
        """Get schema for fixture step - basic fields only."""
        # Build universe options from added universes
        universe_options = (
            {k: f"Universe {k}" for k in sorted(self._universes.keys())}
            if self._universes
            else {"1": "Universe 1"}
        )

        return vol.Schema(
            {
                vol.Required("universe", default=list(universe_options.keys())[0]): vol.In(
                    universe_options
                ),
                # Name and channel are optional in schema (validated in backend for "add" action)
                vol.Optional(CONF_NAME, default=""): str,
                vol.Required(CONF_TYPE, default=LIGHT_TYPE_DIMMER): vol.In(
                    {k: LIGHT_TYPE_LABELS[k] for k in LIGHT_TYPES}
                ),
                vol.Optional(CONF_CHANNEL, default=MIN_CHANNEL): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_CHANNEL, max=MAX_CHANNEL)
                ),
                vol.Optional(CONF_TRANSITION, default=DEFAULT_TRANSITION): vol.All(
                    vol.Coerce(float),
                    vol.Range(min=MIN_TRANSITION, max=MAX_TRANSITION),
                ),
                vol.Optional(
                    CONF_OUTPUT_CORRECTION, default=""
                ): vol.In(
                    {"": "(Use Universe Default)", **{k: OUTPUT_CORRECTION_LABELS[k] for k in OUTPUT_CORRECTIONS}}
                ),
                vol.Optional(CONF_CHANNEL_SIZE, default=DEFAULT_CHANNEL_SIZE): vol.In(
                    {k: CHANNEL_SIZE_LABELS[k] for k in CHANNEL_SIZES}
                ),
                vol.Optional(CONF_BYTE_ORDER, default=DEFAULT_BYTE_ORDER): vol.In(
                    {k: BYTE_ORDER_LABELS[k] for k in BYTE_ORDERS}
                ),
                vol.Required("action", default="add"): vol.In(
                    {"add": "Add Fixture", "done": "Done - Review Configuration"}
                ),
            }
        )

    def _get_fixture_details_schema(self, fixture_type: str) -> vol.Schema:
        """Get schema for type-specific fixture details."""
        schema_dict: dict[Any, Any] = {}

        # Color temperature types need min/max temp
        if fixture_type in (LIGHT_TYPE_COLOR_TEMP, LIGHT_TYPE_RGBWW):
            schema_dict[vol.Required(CONF_MIN_TEMP, default=DEFAULT_MIN_TEMP)] = str
            schema_dict[vol.Required(CONF_MAX_TEMP, default=DEFAULT_MAX_TEMP)] = str

        # Fixed type needs channel count
        if fixture_type == LIGHT_TYPE_FIXED:
            schema_dict[vol.Required(CONF_CHANNEL_COUNT, default=DEFAULT_CHANNEL_COUNT)] = vol.All(
                vol.Coerce(int), vol.Range(min=1, max=MAX_FIXED_CHANNELS)
            )

        # Channel setup with type-appropriate default hint
        default_setup = DEFAULT_CHANNEL_SETUPS.get(fixture_type, "")
        if isinstance(default_setup, str) and default_setup:
            # Show default for this type as placeholder hint
            schema_dict[vol.Optional(CONF_CHANNEL_SETUP, default=default_setup)] = str
        else:
            schema_dict[vol.Optional(CONF_CHANNEL_SETUP)] = str

        return vol.Schema(schema_dict)

    def _validate_fixture_basic(self, data: dict[str, Any]) -> dict[str, str]:
        """Validate basic fixture settings."""
        errors: dict[str, str] = {}

        if not data.get(CONF_NAME):
            errors[CONF_NAME] = "name_required"

        channel = data.get(CONF_CHANNEL)
        if channel is None or not (MIN_CHANNEL <= channel <= MAX_CHANNEL):
            errors[CONF_CHANNEL] = "invalid_channel"

        return errors

    def _validate_fixture_details(self, data: dict[str, Any], fixture_type: str) -> dict[str, str]:
        """Validate type-specific fixture details."""
        errors: dict[str, str] = {}

        # Validate temperature format for color temp types
        if fixture_type in (LIGHT_TYPE_COLOR_TEMP, LIGHT_TYPE_RGBWW):
            min_temp = data.get(CONF_MIN_TEMP, "")
            max_temp = data.get(CONF_MAX_TEMP, "")
            if not min_temp:
                errors[CONF_MIN_TEMP] = "temp_required"
            elif not self._is_valid_temp_format(min_temp):
                errors[CONF_MIN_TEMP] = "invalid_temp_format"
            if not max_temp:
                errors[CONF_MAX_TEMP] = "temp_required"
            elif not self._is_valid_temp_format(max_temp):
                errors[CONF_MAX_TEMP] = "invalid_temp_format"

        # Validate channel count for fixed type
        if fixture_type == LIGHT_TYPE_FIXED:
            channel_count = data.get(CONF_CHANNEL_COUNT)
            if channel_count is None or not (1 <= channel_count <= MAX_FIXED_CHANNELS):
                errors[CONF_CHANNEL_COUNT] = "invalid_channel_count"

        return errors

    @staticmethod
    def _is_valid_temp_format(temp: str) -> bool:
        """Validate temperature format (e.g., '2700K')."""
        if not temp:
            return True
        temp = temp.strip().upper()
        if not temp.endswith("K"):
            return False
        try:
            int(temp[:-1])
            return True
        except ValueError:
            return False

    def _build_channel_setup(self, data: dict[str, Any]) -> str | None:
        """Build channel_setup string from fixture data."""
        fixture_type = data.get(CONF_TYPE)

        # If channel_setup is provided, use it
        if data.get(CONF_CHANNEL_SETUP):
            return data[CONF_CHANNEL_SETUP]

        # Otherwise return default for type
        default = DEFAULT_CHANNEL_SETUPS.get(fixture_type)
        if isinstance(default, str):
            return default
        return None

    # ─────────────────────────────────────────────────────────────────
    # STEP 4: REVIEW
    # ─────────────────────────────────────────────────────────────────
    async def async_step_review(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle review step before saving."""
        if user_input is not None:
            action = user_input.get("action", "submit")

            if action == "back":
                return await self.async_step_fixture()

            # Submit - create entry
            config_data = self._build_config_data()

            # Generate unique ID
            node_type = self._connection_data.get(CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT)
            port = self._connection_data.get(CONF_PORT, DEFAULT_PORTS.get(node_type, 6454))
            unique_id = f"{self._connection_data[CONF_HOST]}:{port}"

            await self.async_set_unique_id(unique_id)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=f"Art-Net {self._connection_data[CONF_HOST]}",
                data=config_data,
            )

        # Build summary for display
        summary = self._build_summary()

        return self.async_show_form(
            step_id="review",
            data_schema=vol.Schema(
                {
                    vol.Required("action", default="submit"): vol.In(
                        {"submit": "Create Integration", "back": "Go Back to Edit"}
                    ),
                }
            ),
            description_placeholders={"summary": summary},
        )

    def _build_config_data(self) -> dict[str, Any]:
        """Build final configuration data for config entry."""
        # Organize fixtures into universes
        for fixture in self._fixtures:
            universe = str(fixture.pop("universe", "1"))
            if universe not in self._universes:
                self._universes[universe] = {
                    CONF_OUTPUT_CORRECTION: DEFAULT_OUTPUT_CORRECTION,
                    CONF_SEND_PARTIAL_UNIVERSE: DEFAULT_SEND_PARTIAL_UNIVERSE,
                    CONF_DEVICES: [],
                }
            # Remove empty output_correction
            if fixture.get(CONF_OUTPUT_CORRECTION) == "":
                fixture.pop(CONF_OUTPUT_CORRECTION, None)
            self._universes[universe][CONF_DEVICES].append(fixture)

        # Build final config
        node_type = self._connection_data.get(CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT)
        port = self._connection_data.get(CONF_PORT, DEFAULT_PORTS.get(node_type, 6454))

        config = {
            CONF_HOST: self._connection_data[CONF_HOST],
            CONF_PORT: port,
            CONF_NODE_TYPE: node_type,
            CONF_MAX_FPS: self._connection_data.get(CONF_MAX_FPS, DEFAULT_MAX_FPS),
            CONF_REFRESH_EVERY: self._connection_data.get(
                CONF_REFRESH_EVERY, DEFAULT_REFRESH_EVERY
            ),
            CONF_UNIVERSES: self._universes,
        }

        # Add optional overrides
        if self._connection_data.get(CONF_HOST_OVERRIDE):
            config[CONF_HOST_OVERRIDE] = self._connection_data[CONF_HOST_OVERRIDE]
        if self._connection_data.get(CONF_PORT_OVERRIDE):
            config[CONF_PORT_OVERRIDE] = self._connection_data[CONF_PORT_OVERRIDE]

        return config

    def _build_summary(self) -> str:
        """Build summary string for review step."""
        lines = []

        # Connection info
        node_type = self._connection_data.get(CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT)
        port = self._connection_data.get(CONF_PORT, DEFAULT_PORTS.get(node_type, 6454))
        lines.append(f"**Connection:** {self._connection_data.get(CONF_HOST)}:{port}")
        lines.append(f"**Protocol:** {NODE_TYPE_LABELS.get(node_type, node_type)}")
        lines.append(f"**FPS:** {self._connection_data.get(CONF_MAX_FPS, DEFAULT_MAX_FPS)}")
        lines.append("")

        # Universe and fixture summary
        # Group fixtures by universe
        fixtures_by_universe: dict[str, list[dict]] = {}
        for fixture in self._fixtures:
            universe = str(fixture.get("universe", "1"))
            if universe not in fixtures_by_universe:
                fixtures_by_universe[universe] = []
            fixtures_by_universe[universe].append(fixture)

        for universe_num in sorted(fixtures_by_universe.keys()):
            fixtures = fixtures_by_universe[universe_num]
            lines.append(f"**Universe {universe_num}:** {len(fixtures)} fixture(s)")
            for fixture in fixtures:
                name = fixture.get(CONF_NAME, "Unnamed")
                ftype = LIGHT_TYPE_LABELS.get(fixture.get(CONF_TYPE, ""), fixture.get(CONF_TYPE, ""))
                channel = fixture.get(CONF_CHANNEL, "?")
                lines.append(f"  - {name} ({ftype}, Ch: {channel})")
            lines.append("")

        lines.append(f"**Total:** {len(self._fixtures)} fixture(s)")

        return "\n".join(lines)

    # ─────────────────────────────────────────────────────────────────
    # OPTIONS FLOW
    # ─────────────────────────────────────────────────────────────────
    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> ArtNetLedOptionsFlow:
        """Get the options flow for this handler."""
        return ArtNetLedOptionsFlow(config_entry)


class ArtNetLedOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for Art-Net LED."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry
        self._connection_data: dict[str, Any] = {}
        self._universes: dict[str, dict[str, Any]] = {}
        self._fixtures: list[dict[str, Any]] = []
        self._load_existing_config()

    def _load_existing_config(self) -> None:
        """Load existing configuration from config entry."""
        data = dict(self.config_entry.data)

        # Extract connection data
        self._connection_data = {
            CONF_HOST: data.get(CONF_HOST, ""),
            CONF_PORT: data.get(CONF_PORT),
            CONF_NODE_TYPE: data.get(CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT),
            CONF_MAX_FPS: data.get(CONF_MAX_FPS, DEFAULT_MAX_FPS),
            CONF_REFRESH_EVERY: data.get(CONF_REFRESH_EVERY, DEFAULT_REFRESH_EVERY),
            CONF_HOST_OVERRIDE: data.get(CONF_HOST_OVERRIDE),
            CONF_PORT_OVERRIDE: data.get(CONF_PORT_OVERRIDE),
        }

        # Extract universes and fixtures
        self._universes = {}
        self._fixtures = []

        for universe_num, universe_data in data.get(CONF_UNIVERSES, {}).items():
            self._universes[universe_num] = {
                CONF_OUTPUT_CORRECTION: universe_data.get(
                    CONF_OUTPUT_CORRECTION, DEFAULT_OUTPUT_CORRECTION
                ),
                CONF_SEND_PARTIAL_UNIVERSE: universe_data.get(
                    CONF_SEND_PARTIAL_UNIVERSE, DEFAULT_SEND_PARTIAL_UNIVERSE
                ),
                CONF_DEVICES: [],
            }
            for device in universe_data.get(CONF_DEVICES, []):
                fixture = dict(device)
                fixture["universe"] = universe_num
                self._fixtures.append(fixture)

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle options flow initialization."""
        if user_input is not None:
            action = user_input.get("action")
            if action == "connection":
                return await self.async_step_connection()
            elif action == "universes":
                return await self.async_step_universe()
            elif action == "fixtures":
                return await self.async_step_fixture()

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required("action"): vol.In(
                        {
                            "connection": "Edit Connection Settings",
                            "universes": "Edit Universes",
                            "fixtures": "Edit Fixtures",
                        }
                    ),
                }
            ),
        )

    async def async_step_connection(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle connection editing."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Validate and save
            if ArtNetLedConfigFlow._is_valid_ipv4(user_input.get(CONF_HOST, "")):
                self._connection_data.update(user_input)
                return await self._save_options()
            else:
                errors[CONF_HOST] = "invalid_host"

        # Pre-fill with existing values
        return self.async_show_form(
            step_id="connection",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_HOST, default=self._connection_data.get(CONF_HOST, "")
                    ): str,
                    vol.Required(
                        CONF_NODE_TYPE,
                        default=self._connection_data.get(
                            CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT
                        ),
                    ): vol.In({k: NODE_TYPE_LABELS[k] for k in NODE_TYPES}),
                    vol.Optional(
                        CONF_PORT, default=self._connection_data.get(CONF_PORT)
                    ): vol.Coerce(int),
                    vol.Optional(
                        CONF_MAX_FPS,
                        default=self._connection_data.get(CONF_MAX_FPS, DEFAULT_MAX_FPS),
                    ): vol.All(vol.Coerce(int), vol.Range(min=MIN_FPS, max=MAX_FPS)),
                    vol.Optional(
                        CONF_REFRESH_EVERY,
                        default=self._connection_data.get(
                            CONF_REFRESH_EVERY, DEFAULT_REFRESH_EVERY
                        ),
                    ): vol.All(
                        vol.Coerce(float), vol.Range(min=MIN_REFRESH, max=MAX_REFRESH)
                    ),
                }
            ),
            errors=errors,
        )

    async def async_step_universe(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle universe editing - list, add, edit, delete."""
        errors: dict[str, str] = {}

        if user_input is not None:
            action = user_input.get("action", "back")

            if action == "back":
                return await self.async_step_init()

            elif action == "add":
                return await self.async_step_universe_edit()

            elif action.startswith("edit_"):
                universe_num = action.replace("edit_", "")
                self._editing_universe = universe_num
                return await self.async_step_universe_edit()

            elif action.startswith("delete_"):
                universe_num = action.replace("delete_", "")
                if universe_num in self._universes:
                    # Remove fixtures in this universe
                    self._fixtures = [f for f in self._fixtures if f.get("universe") != universe_num]
                    del self._universes[universe_num]
                return await self.async_step_universe()

        # Build action options - list current universes
        actions: dict[str, str] = {}
        for uni_num in sorted(self._universes.keys()):
            fixture_count = len([f for f in self._fixtures if f.get("universe") == uni_num])
            actions[f"edit_{uni_num}"] = f"Edit Universe {uni_num} ({fixture_count} fixtures)"
            actions[f"delete_{uni_num}"] = f"Delete Universe {uni_num}"
        actions["add"] = "Add New Universe"
        actions["back"] = "Back to Menu"

        return self.async_show_form(
            step_id="universe",
            data_schema=vol.Schema({vol.Required("action"): vol.In(actions)}),
            errors=errors,
            description_placeholders={
                "universe_count": str(len(self._universes)),
            },
        )

    async def async_step_universe_edit(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle editing a single universe."""
        errors: dict[str, str] = {}
        editing = getattr(self, "_editing_universe", None)

        if user_input is not None:
            universe_num = str(user_input.get(CONF_UNIVERSE_NUMBER, 1))
            self._universes[universe_num] = {
                CONF_OUTPUT_CORRECTION: user_input.get(CONF_OUTPUT_CORRECTION, DEFAULT_OUTPUT_CORRECTION),
                CONF_SEND_PARTIAL_UNIVERSE: user_input.get(CONF_SEND_PARTIAL_UNIVERSE, DEFAULT_SEND_PARTIAL_UNIVERSE),
                CONF_DEVICES: self._universes.get(universe_num, {}).get(CONF_DEVICES, []),
            }
            # Update fixture universe references if number changed
            if editing and editing != universe_num:
                for fixture in self._fixtures:
                    if fixture.get("universe") == editing:
                        fixture["universe"] = universe_num
                if editing in self._universes:
                    del self._universes[editing]
            self._editing_universe = None
            return await self.async_step_universe()

        # Pre-fill with existing values if editing
        defaults = self._universes.get(editing, {}) if editing else {}

        return self.async_show_form(
            step_id="universe_edit",
            data_schema=vol.Schema({
                vol.Required(
                    CONF_UNIVERSE_NUMBER,
                    default=int(editing) if editing else 1
                ): vol.All(vol.Coerce(int), vol.Range(min=MIN_UNIVERSE, max=MAX_UNIVERSE)),
                vol.Required(
                    CONF_OUTPUT_CORRECTION,
                    default=defaults.get(CONF_OUTPUT_CORRECTION, DEFAULT_OUTPUT_CORRECTION)
                ): vol.In({k: OUTPUT_CORRECTION_LABELS[k] for k in OUTPUT_CORRECTIONS}),
                vol.Required(
                    CONF_SEND_PARTIAL_UNIVERSE,
                    default=defaults.get(CONF_SEND_PARTIAL_UNIVERSE, DEFAULT_SEND_PARTIAL_UNIVERSE)
                ): bool,
            }),
            errors=errors,
        )

    async def async_step_fixture(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle fixture editing - list, add, edit, delete."""
        errors: dict[str, str] = {}

        if user_input is not None:
            action = user_input.get("action", "back")

            if action == "back":
                return await self.async_step_init()

            elif action == "add":
                return await self.async_step_fixture_add()

            elif action.startswith("edit_"):
                fixture_idx = int(action.replace("edit_", ""))
                self._editing_fixture_idx = fixture_idx
                return await self.async_step_fixture_edit()

            elif action.startswith("delete_"):
                fixture_idx = int(action.replace("delete_", ""))
                if 0 <= fixture_idx < len(self._fixtures):
                    del self._fixtures[fixture_idx]
                return await self.async_step_fixture()

        # Build action options - list current fixtures
        actions: dict[str, str] = {}
        for idx, fixture in enumerate(self._fixtures):
            name = fixture.get(CONF_NAME, f"Fixture {idx + 1}")
            ftype = LIGHT_TYPE_LABELS.get(fixture.get(CONF_TYPE, ""), fixture.get(CONF_TYPE, ""))
            channel = fixture.get(CONF_CHANNEL, "?")
            actions[f"edit_{idx}"] = f"Edit: {name} ({ftype}, Ch: {channel})"
            actions[f"delete_{idx}"] = f"Delete: {name}"
        actions["add"] = "Add New Fixture"
        actions["back"] = "Back to Menu"

        return self.async_show_form(
            step_id="fixture",
            data_schema=vol.Schema({vol.Required("action"): vol.In(actions)}),
            errors=errors,
            description_placeholders={
                "fixture_count": str(len(self._fixtures)),
            },
        )

    async def async_step_fixture_add(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Add a new fixture in options flow."""
        errors: dict[str, str] = {}

        if user_input is not None:
            # Validate
            if not user_input.get(CONF_NAME):
                errors[CONF_NAME] = "name_required"
            if not errors:
                fixture_data = dict(user_input)
                fixture_data[CONF_FIXTURE_ID] = str(uuid.uuid4())
                # Build channel_setup
                fixture_type = fixture_data.get(CONF_TYPE, LIGHT_TYPE_DIMMER)
                if fixture_type in DEFAULT_CHANNEL_SETUPS:
                    default_setup = DEFAULT_CHANNEL_SETUPS[fixture_type]
                    if isinstance(default_setup, str):
                        fixture_data[CONF_CHANNEL_SETUP] = default_setup
                self._fixtures.append(fixture_data)
                return await self.async_step_fixture()

        # Build universe options
        universe_options = {k: f"Universe {k}" for k in sorted(self._universes.keys())} or {"1": "Universe 1"}

        return self.async_show_form(
            step_id="fixture_add",
            data_schema=vol.Schema({
                vol.Required("universe", default=list(universe_options.keys())[0]): vol.In(universe_options),
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_TYPE, default=LIGHT_TYPE_DIMMER): vol.In(
                    {k: LIGHT_TYPE_LABELS[k] for k in LIGHT_TYPES}
                ),
                vol.Required(CONF_CHANNEL, default=MIN_CHANNEL): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_CHANNEL, max=MAX_CHANNEL)
                ),
                vol.Optional(CONF_TRANSITION, default=DEFAULT_TRANSITION): vol.All(
                    vol.Coerce(float), vol.Range(min=MIN_TRANSITION, max=MAX_TRANSITION)
                ),
            }),
            errors=errors,
        )

    async def async_step_fixture_edit(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Edit an existing fixture in options flow."""
        errors: dict[str, str] = {}
        fixture_idx = getattr(self, "_editing_fixture_idx", 0)

        if fixture_idx >= len(self._fixtures):
            return await self.async_step_fixture()

        current_fixture = self._fixtures[fixture_idx]

        if user_input is not None:
            # Validate
            if not user_input.get(CONF_NAME):
                errors[CONF_NAME] = "name_required"
            if not errors:
                # Update fixture
                current_fixture.update(user_input)
                # Rebuild channel_setup
                fixture_type = current_fixture.get(CONF_TYPE, LIGHT_TYPE_DIMMER)
                if fixture_type in DEFAULT_CHANNEL_SETUPS:
                    default_setup = DEFAULT_CHANNEL_SETUPS[fixture_type]
                    if isinstance(default_setup, str):
                        current_fixture[CONF_CHANNEL_SETUP] = default_setup
                self._editing_fixture_idx = None
                return await self.async_step_fixture()

        # Build universe options
        universe_options = {k: f"Universe {k}" for k in sorted(self._universes.keys())} or {"1": "Universe 1"}

        return self.async_show_form(
            step_id="fixture_edit",
            data_schema=vol.Schema({
                vol.Required("universe", default=current_fixture.get("universe", "1")): vol.In(universe_options),
                vol.Required(CONF_NAME, default=current_fixture.get(CONF_NAME, "")): str,
                vol.Required(CONF_TYPE, default=current_fixture.get(CONF_TYPE, LIGHT_TYPE_DIMMER)): vol.In(
                    {k: LIGHT_TYPE_LABELS[k] for k in LIGHT_TYPES}
                ),
                vol.Required(CONF_CHANNEL, default=current_fixture.get(CONF_CHANNEL, MIN_CHANNEL)): vol.All(
                    vol.Coerce(int), vol.Range(min=MIN_CHANNEL, max=MAX_CHANNEL)
                ),
                vol.Optional(CONF_TRANSITION, default=current_fixture.get(CONF_TRANSITION, DEFAULT_TRANSITION)): vol.All(
                    vol.Coerce(float), vol.Range(min=MIN_TRANSITION, max=MAX_TRANSITION)
                ),
            }),
            errors=errors,
            description_placeholders={
                "fixture_name": current_fixture.get(CONF_NAME, "Fixture"),
            },
        )

    async def _save_options(self) -> FlowResult:
        """Save options and update config entry."""
        # Rebuild config data
        # Clear devices from universes first
        for universe_data in self._universes.values():
            universe_data[CONF_DEVICES] = []

        # Re-add fixtures to universes
        for fixture in self._fixtures:
            universe = str(fixture.pop("universe", "1"))
            if universe not in self._universes:
                self._universes[universe] = {
                    CONF_OUTPUT_CORRECTION: DEFAULT_OUTPUT_CORRECTION,
                    CONF_SEND_PARTIAL_UNIVERSE: DEFAULT_SEND_PARTIAL_UNIVERSE,
                    CONF_DEVICES: [],
                }
            self._universes[universe][CONF_DEVICES].append(fixture)

        # Build new config
        node_type = self._connection_data.get(CONF_NODE_TYPE, NODE_TYPE_ARTNET_DIRECT)
        port = self._connection_data.get(CONF_PORT, DEFAULT_PORTS.get(node_type, 6454))

        new_data = {
            CONF_HOST: self._connection_data[CONF_HOST],
            CONF_PORT: port,
            CONF_NODE_TYPE: node_type,
            CONF_MAX_FPS: self._connection_data.get(CONF_MAX_FPS, DEFAULT_MAX_FPS),
            CONF_REFRESH_EVERY: self._connection_data.get(
                CONF_REFRESH_EVERY, DEFAULT_REFRESH_EVERY
            ),
            CONF_UNIVERSES: self._universes,
        }

        # Add optional overrides
        if self._connection_data.get(CONF_HOST_OVERRIDE):
            new_data[CONF_HOST_OVERRIDE] = self._connection_data[CONF_HOST_OVERRIDE]
        if self._connection_data.get(CONF_PORT_OVERRIDE):
            new_data[CONF_PORT_OVERRIDE] = self._connection_data[CONF_PORT_OVERRIDE]

        # Update config entry
        self.hass.config_entries.async_update_entry(
            self.config_entry,
            data=new_data,
        )

        return self.async_create_entry(title="", data={})

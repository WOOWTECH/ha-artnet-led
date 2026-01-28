"""Art-Net LED integration for Home Assistant."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Art-Net LED from YAML configuration (backward compatible)."""
    # YAML setup is handled by the light platform directly via async_setup_platform
    # This function just needs to return True to indicate the domain is set up
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Art-Net LED from a config entry."""
    _LOGGER.debug("Setting up Art-Net LED config entry: %s", entry.entry_id)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "config": entry.data,
        "node": None,  # Will be set by light platform
        "entities": [],
    }

    # Forward setup to light platform
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register update listener for options flow
    entry.async_on_unload(entry.add_update_listener(async_update_options))

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug("Unloading Art-Net LED config entry: %s", entry.entry_id)

    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        # Clean up stored data
        entry_data = hass.data[DOMAIN].pop(entry.entry_id, {})

        # Close pyartnet node if it exists
        node = entry_data.get("node")
        if node is not None:
            try:
                await node.stop()
            except Exception as err:
                _LOGGER.warning("Error stopping Art-Net node: %s", err)

    return unload_ok


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    _LOGGER.debug("Reloading Art-Net LED config entry due to options update")
    await hass.config_entries.async_reload(entry.entry_id)

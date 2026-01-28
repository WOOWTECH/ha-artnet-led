"""Constants for Art-Net LED integration."""
from __future__ import annotations

from typing import Final

DOMAIN: Final = "artnet_led"

# Platforms
PLATFORMS: Final = ["light"]

# Protocols / Node Types
CONF_NODE_TYPE: Final = "node_type"
NODE_TYPE_ARTNET_DIRECT: Final = "artnet-direct"
NODE_TYPE_ARTNET_CONTROLLER: Final = "artnet-controller"
NODE_TYPE_SACN: Final = "sacn"
NODE_TYPE_KINET: Final = "kinet"

NODE_TYPES: Final = [
    NODE_TYPE_ARTNET_DIRECT,
    NODE_TYPE_ARTNET_CONTROLLER,
    NODE_TYPE_SACN,
    NODE_TYPE_KINET,
]

NODE_TYPE_LABELS: Final = {
    NODE_TYPE_ARTNET_DIRECT: "Art-Net Direct",
    NODE_TYPE_ARTNET_CONTROLLER: "Art-Net Controller",
    NODE_TYPE_SACN: "sACN (E1.31)",
    NODE_TYPE_KINET: "KiNet",
}

# Default ports by protocol
DEFAULT_PORTS: Final = {
    NODE_TYPE_ARTNET_DIRECT: 6454,
    NODE_TYPE_ARTNET_CONTROLLER: 6454,
    NODE_TYPE_SACN: 5568,
    NODE_TYPE_KINET: 6038,
}

# Light types
LIGHT_TYPE_BINARY: Final = "binary"
LIGHT_TYPE_DIMMER: Final = "dimmer"
LIGHT_TYPE_COLOR_TEMP: Final = "color_temp"
LIGHT_TYPE_RGB: Final = "rgb"
LIGHT_TYPE_RGBW: Final = "rgbw"
LIGHT_TYPE_RGBWW: Final = "rgbww"
LIGHT_TYPE_XY: Final = "xy"
LIGHT_TYPE_FIXED: Final = "fixed"

LIGHT_TYPES: Final = [
    LIGHT_TYPE_BINARY,
    LIGHT_TYPE_DIMMER,
    LIGHT_TYPE_COLOR_TEMP,
    LIGHT_TYPE_RGB,
    LIGHT_TYPE_RGBW,
    LIGHT_TYPE_RGBWW,
    LIGHT_TYPE_XY,
    LIGHT_TYPE_FIXED,
]

LIGHT_TYPE_LABELS: Final = {
    LIGHT_TYPE_BINARY: "Binary (On/Off)",
    LIGHT_TYPE_DIMMER: "Dimmer",
    LIGHT_TYPE_COLOR_TEMP: "Color Temperature",
    LIGHT_TYPE_RGB: "RGB",
    LIGHT_TYPE_RGBW: "RGBW",
    LIGHT_TYPE_RGBWW: "RGBWW",
    LIGHT_TYPE_XY: "XY Color Space",
    LIGHT_TYPE_FIXED: "Fixed Output",
}

# Default channel setups per type (from code analysis)
DEFAULT_CHANNEL_SETUPS: Final = {
    LIGHT_TYPE_DIMMER: "d",
    LIGHT_TYPE_COLOR_TEMP: "ch",  # cold + hot white
    LIGHT_TYPE_RGB: "rgb",
    LIGHT_TYPE_RGBW: "rgbw",
    LIGHT_TYPE_RGBWW: "rgbch",
    LIGHT_TYPE_XY: "dxy",  # dimmer + x + y
    LIGHT_TYPE_FIXED: [255],
}

# Channel counts per type
CHANNEL_COUNTS: Final = {
    LIGHT_TYPE_BINARY: 1,
    LIGHT_TYPE_DIMMER: 1,
    LIGHT_TYPE_COLOR_TEMP: 2,
    LIGHT_TYPE_RGB: 3,
    LIGHT_TYPE_RGBW: 4,
    LIGHT_TYPE_RGBWW: 5,
    LIGHT_TYPE_XY: 3,  # d + x + y
    LIGHT_TYPE_FIXED: None,  # Variable - user specified
}

# Output corrections
OUTPUT_CORRECTION_LINEAR: Final = "linear"
OUTPUT_CORRECTION_QUADRATIC: Final = "quadratic"
OUTPUT_CORRECTION_CUBIC: Final = "cubic"
OUTPUT_CORRECTION_QUADRUPLE: Final = "quadruple"

OUTPUT_CORRECTIONS: Final = [
    OUTPUT_CORRECTION_LINEAR,
    OUTPUT_CORRECTION_QUADRATIC,
    OUTPUT_CORRECTION_CUBIC,
    OUTPUT_CORRECTION_QUADRUPLE,
]

OUTPUT_CORRECTION_LABELS: Final = {
    OUTPUT_CORRECTION_LINEAR: "Linear",
    OUTPUT_CORRECTION_QUADRATIC: "Quadratic",
    OUTPUT_CORRECTION_CUBIC: "Cubic",
    OUTPUT_CORRECTION_QUADRUPLE: "Quadruple",
}

# Channel sizes
CHANNEL_SIZE_8BIT: Final = "8bit"
CHANNEL_SIZE_16BIT: Final = "16bit"
CHANNEL_SIZE_24BIT: Final = "24bit"
CHANNEL_SIZE_32BIT: Final = "32bit"

CHANNEL_SIZES: Final = [
    CHANNEL_SIZE_8BIT,
    CHANNEL_SIZE_16BIT,
    CHANNEL_SIZE_24BIT,
    CHANNEL_SIZE_32BIT,
]

CHANNEL_SIZE_LABELS: Final = {
    CHANNEL_SIZE_8BIT: "8-bit",
    CHANNEL_SIZE_16BIT: "16-bit",
    CHANNEL_SIZE_24BIT: "24-bit",
    CHANNEL_SIZE_32BIT: "32-bit",
}

# Byte orders
BYTE_ORDER_BIG: Final = "big"
BYTE_ORDER_LITTLE: Final = "little"

BYTE_ORDERS: Final = [BYTE_ORDER_BIG, BYTE_ORDER_LITTLE]

BYTE_ORDER_LABELS: Final = {
    BYTE_ORDER_BIG: "Big Endian",
    BYTE_ORDER_LITTLE: "Little Endian",
}

# Channel setup codes (updated with Hue/Saturation)
CHANNEL_SETUP_CODES: Final = {
    "d": "Dimmer",
    "r": "Red (scaled)",
    "R": "Red (unscaled)",
    "g": "Green (scaled)",
    "G": "Green (unscaled)",
    "b": "Blue (scaled)",
    "B": "Blue (unscaled)",
    "c": "Cool White (scaled)",
    "C": "Cool White (unscaled)",
    "h": "Warm White (scaled)",
    "H": "Warm White (unscaled)",
    "w": "White Auto (scaled)",
    "W": "White Auto (unscaled)",
    "t": "Temperature (0=warm)",
    "T": "Temperature (0=cold)",
    "x": "X Coordinate",
    "y": "Y Coordinate",
    "u": "Hue",
    "U": "Saturation",
}

# Configuration keys
CONF_HOST: Final = "host"
CONF_PORT: Final = "port"
CONF_MAX_FPS: Final = "max_fps"
CONF_REFRESH_EVERY: Final = "refresh_every"
CONF_HOST_OVERRIDE: Final = "host_override"
CONF_PORT_OVERRIDE: Final = "port_override"
CONF_UNIVERSES: Final = "universes"
CONF_UNIVERSE_NUMBER: Final = "universe_number"
CONF_OUTPUT_CORRECTION: Final = "output_correction"
CONF_SEND_PARTIAL_UNIVERSE: Final = "send_partial_universe"
CONF_DEVICES: Final = "devices"
CONF_FIXTURE_ID: Final = "fixture_id"
CONF_CHANNEL: Final = "channel"
CONF_NAME: Final = "name"
CONF_TYPE: Final = "type"
CONF_TRANSITION: Final = "transition"
CONF_CHANNEL_SIZE: Final = "channel_size"
CONF_BYTE_ORDER: Final = "byte_order"
CONF_CHANNEL_SETUP: Final = "channel_setup"
CONF_CHANNEL_COUNT: Final = "channel_count"
CONF_MIN_TEMP: Final = "min_temp"
CONF_MAX_TEMP: Final = "max_temp"

# Defaults
DEFAULT_MAX_FPS: Final = 25
DEFAULT_REFRESH_EVERY: Final = 120
DEFAULT_TRANSITION: Final = 0.0
DEFAULT_OUTPUT_CORRECTION: Final = OUTPUT_CORRECTION_LINEAR
DEFAULT_CHANNEL_SIZE: Final = CHANNEL_SIZE_8BIT
DEFAULT_BYTE_ORDER: Final = BYTE_ORDER_BIG
DEFAULT_SEND_PARTIAL_UNIVERSE: Final = True
DEFAULT_MIN_TEMP: Final = "2700K"
DEFAULT_MAX_TEMP: Final = "6500K"
DEFAULT_CHANNEL_COUNT: Final = 1

# Validation limits
MIN_UNIVERSE: Final = 0
MAX_UNIVERSE: Final = 1024
MIN_CHANNEL: Final = 1
MAX_CHANNEL: Final = 512
MIN_FPS: Final = 1
MAX_FPS: Final = 50
MIN_REFRESH: Final = 0
MAX_REFRESH: Final = 9999
MIN_PORT: Final = 1
MAX_PORT: Final = 65535
MIN_TRANSITION: Final = 0
MAX_TRANSITION: Final = 999
MAX_FIXED_CHANNELS: Final = 16

# Sound Pillow
# KMK firmware
# XIAO RP2040
#
# 12 keys:
# F13 - F24
#
# Rotary encoder:
# clockwise  = Volume Up
# counterclockwise = Volume Down
#
# 7x SK6812MINI-E:
# rainbow animation
#
# LED visual order:
# D9 -> D15 -> D14 -> D11 -> D10 -> D12 -> D13

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB


keyboard = KMKKeyboard()


# ============================================================
# MATRIX
# ============================================================

keyboard.col_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
)

keyboard.row_pins = (
    board.D4,
    board.D5,
    board.D6,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


# ============================================================
# KEYMAP
# ============================================================

keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15, KC.F16,
        KC.F17, KC.F18, KC.F19, KC.F20,
        KC.F21, KC.F22, KC.F23, KC.F24,
    ]
]


# ============================================================
# ROTARY ENCODER
# ============================================================

encoder_handler = EncoderHandler()

encoder_handler.pins = (
    (board.D7, board.D8, None),
)

encoder_handler.map = [
    (
        (KC.VOLU, KC.VOLD),
    ),
]

keyboard.modules.append(encoder_handler)


# ============================================================
# RGB / SK6812MINI-E
# ============================================================

rgb = RGB(
    pixel_pin=board.D9,
    num_pixels=7,
    rgb_order=(1, 0, 2),
)

rgb.effect = "rainbow"

rgb.animation_mode = 1

rgb.brightness = 0.25

keyboard.extensions.append(rgb)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    keyboard.go()
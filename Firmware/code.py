import board
import neopixel

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# ---------------- Keyboard ----------------
keyboard = KMKKeyboard()

# ---------------- Keys ----------------
PINS = (
    board.D1,  # M
    board.D2,  # I
    board.D3,  # G
    board.D7,  # U
    board.D8,  # E
    board.D9,  # L
)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [[
    KC.M,
    KC.I,
    KC.G,
    KC.U,
    KC.E,
    KC.L,
]]

# ---------------- LEDs ----------------
pixels = neopixel.NeoPixel(
    board.D6,
    2,
    brightness=0.3,
    auto_write=False
)

# Power LED
pixels[0] = (0, 255, 0)
pixels.show()

def after_key_handler(keyboard, key, is_pressed, *args):
    if is_pressed:
        pixels[1] = (0, 0, 255)
        pixels.show()

keyboard.after_key_press_handler = after_key_handler

# ---------------- Start ----------------
if __name__ == "__main__":
    keyboard.go()
import board
import displayio
import terminalio
from adafruit_display_text import label

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# ---------------- Keyboard ----------------
keyboard = KMKKeyboard()

# ---------------- Keys ----------------
PINS = (
    board.D27,  # M
    board.D28,  # I
    board.D29,  # G
    board.D1,   # U
    board.D2,   # E
    board.D4,   # L
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

# ---------------- OLED ----------------
displayio.release_displays()

i2c = board.I2C()  # SDA=6, SCL=7 automatically
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_ssd1306.SSD1306(
    display_bus, width=128, height=64
)

group = displayio.Group()
display.root_group = group

title = label.Label(
    terminalio.FONT,
    text="Welcome To NTD",
    color=0xFFFFFF,
    x=0,
    y=10
)

typed = label.Label(
    terminalio.FONT,
    text="",
    color=0xFFFFFF,
    x=0,
    y=40
)

group.append(title)
group.append(typed)

typed_text = ""

# ---------------- Key Hook ----------------
def after_key_handler(keyboard, key, is_pressed, *args):
    global typed_text
    if is_pressed and key.code is not None:
        char = key.code
        if isinstance(char, str) and len(char) == 1:
            typed_text += char
            typed_text = typed_text[-16:]  # keep it on screen
            typed.text = typed_text

keyboard.after_key_press_handler = after_key_handler

# ---------------- Start ----------------
if __name__ == "__main__":
    keyboard.go()

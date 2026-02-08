import board
import neopixel
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

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

# ---------------- OLED (SSD1306) ----------------
# Release any previously configured displays
displayio.release_displays()

# I2C pins: SDA=D4, SCL=D5
i2c = busio.I2C(board.D5, board.D4)

# 0.91" common OLED size (change to 64 if your module is 128x64)
WIDTH = 128
HEIGHT = 32

display = None
try:
    # Prefer displayio-backed driver (CircuitPython modern approach)
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    # Rotate display 180 degrees to correct upside-down mounting
    display = adafruit_displayio_ssd1306.SSD1306(
        display_bus, width=WIDTH, height=HEIGHT, rotation=180
    )

    g = displayio.Group()
    text = "Welcome To NTD"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
    # Position roughly centered
    text_area.x = 2
    text_area.y = HEIGHT // 2
    g.append(text_area)
    display.show(g)
except AttributeError:
    # Older builds may not expose displayio.I2CDisplay — fall back to legacy driver
    try:
        import adafruit_ssd1306

        disp = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
        # Try common rotation/flip options on legacy driver
        try:
            disp.rotation = 2
        except Exception:
            try:
                disp.rotate(2)
            except Exception:
                try:
                    disp.rotation = 180
                except Exception:
                    pass
        disp.fill(0)
        try:
            disp.text("Welcome To NTD", 0, HEIGHT // 2, 1)
        except Exception:
            # If text() isn't available, skip drawing text
            pass
        disp.show()
    except Exception:
        # If all display methods fail, leave display as None
        display = None

# ---------------- Start ----------------
if __name__ == "__main__":
    keyboard.go()
    
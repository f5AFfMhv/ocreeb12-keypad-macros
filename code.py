import board
import variables

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB

# KEYBOARD SETUP
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 200
keyboard.modules = [layers, encoders, tapdance]

# SWITCH MATRIX
keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.A2, board.A1, board.A0, False),
                 (board.SCK, board.MISO, board.MOSI, False),)

# EXTENSIONS
rgb_ext = RGB(pixel_pin=board.D10, num_pixels=4, hue_default=180)
keyboard.extensions.append(rgb_ext)
keyboard.debug_enabled = False

# KMK docs: http://kmkfw.io/docs/keycodes/
# MACROS
LANGSW = simple_key_sequence([KC.LCTRL(KC.LSFT(KC.Z))])
FULLSCREEN_WINDOW = simple_key_sequence([KC.LWIN(KC.UP)])
# Personal
PUP = simple_key_sequence([send_string(variables.pu), KC.MACRO_SLEEP_MS(
    50), KC.TAB, KC.MACRO_SLEEP_MS(50), send_string(variables.pp), KC.MACRO_SLEEP_MS(50), KC.ENTER])
PP = simple_key_sequence(
    [send_string(variables.pp), KC.MACRO_SLEEP_MS(50), KC.ENTER])
WRS = simple_key_sequence([send_string(variables.wrs), KC.ENTER, KC.MACRO_SLEEP_MS(500), send_string(
    variables.lp), KC.ENTER, KC.MACRO_SLEEP_MS(500), send_string('sudo -i'), KC.ENTER])
WUP = simple_key_sequence([send_string(variables.wu), KC.MACRO_SLEEP_MS(
    50), KC.TAB, KC.MACRO_SLEEP_MS(50), send_string(variables.wp), KC.MACRO_SLEEP_MS(50), KC.ENTER])
WAUP = simple_key_sequence([send_string(variables.wau), KC.MACRO_SLEEP_MS(
    50), KC.TAB, KC.MACRO_SLEEP_MS(50), send_string(variables.wp), KC.MACRO_SLEEP_MS(50), KC.ENTER])
WP = simple_key_sequence(
    [send_string(variables.lp), KC.MACRO_SLEEP_MS(50), KC.ENTER])
# Workspaces switch
W1 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.HOME))])
W2 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N2))])
W3 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N3))])
W4 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N4))])
W5 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N5))])
W6 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N6))])
W7 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N7))])
W8 = simple_key_sequence([KC.LCMD(KC.LSFT(KC.N8))])
# Change current window position
MOVE_RIGHT = simple_key_sequence(
    [KC.LCMD(KC.RIGHT), KC.MACRO_SLEEP_MS(50), KC.ESC])
MOVE_LEFT = simple_key_sequence(
    [KC.LCMD(KC.LEFT), KC.MACRO_SLEEP_MS(50), KC.ESC])
MOVE_SCREEN_RIGHT = simple_key_sequence(
    [KC.LCMD(KC.LSFT(KC.RIGHT)), KC.MACRO_SLEEP_MS(50), KC.ESC])
MOVE_SCREEN_LEFT = simple_key_sequence(
    [KC.LCMD(KC.LSFT(KC.LEFT)), KC.MACRO_SLEEP_MS(50), KC.ESC])
# Youtube control
# Ctrl+Shift+F1 executes youtube window focus script:
# https://github.com/f5AFfMhv/Random-Scripts/blob/master/HotKey-Deck/youtube_focus.sh
SLOWDOWN = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.LEFT_ANGLE_BRACKET])
SPEEDUP = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.RIGHT_ANGLE_BRACKET])
PREVIOUS = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.LSFT(KC.P)])
NEXT = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.LSFT(KC.N)])
PLAY_PAUSE = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.SPACE])
MINI_PLAYER = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.I])
THEATRE = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.T])
FULLSCREEN = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.F])
FF10 = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.L])
RW10 = simple_key_sequence(
    [KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.J])
PREPARE_WINDOW = simple_key_sequence([KC.LCTRL(KC.LSFT(KC.F1)), KC.MACRO_SLEEP_MS(200), KC.LWIN(
    KC.LSFT(KC.RIGHT)), KC.MACRO_SLEEP_MS(50), KC.LWIN(KC.UP), KC.MACRO_SLEEP_MS(50), KC.F])

# LAYER SWITCHING TAP DANCE
TD_Y_SPEED = KC.TD(SPEEDUP, SLOWDOWN)
TD_Y_VID = KC.TD(NEXT, PREVIOUS)
TD_Y_SCREEN = KC.TD(FULLSCREEN, THEATRE, MINI_PLAYER)
TD_Y_PLAY = KC.TD(PLAY_PAUSE, PREPARE_WINDOW)

TD_W_P = KC.TD(WUP, WAUP)
TD_W_C = KC.TD(WP, WRS)
TD_P_P = KC.TD(PP, PUP)

TD_W_RIGHT = KC.TD(MOVE_RIGHT, MOVE_SCREEN_RIGHT)
TD_W_LEFT = KC.TD(MOVE_LEFT, MOVE_SCREEN_LEFT)

TD_W15 = KC.TD(W1, W5)
TD_W26 = KC.TD(W2, W6)
TD_W37 = KC.TD(W3, W7)
TD_W48 = KC.TD(W4, W8)

TD_OTHER = KC.TD(LANGSW, FULLSCREEN_WINDOW)

# KEYMAPS
keyboard.keymap = [
    [
        TD_W15,         TD_W26,         TD_W37,         TD_W48,
        TD_Y_PLAY,      TD_Y_SCREEN,    TD_Y_SPEED,     TD_Y_VID,
        TD_P_P,         TD_OTHER,       TD_W_C,         TD_W_P,
    ]
]

encoders.map = [
    (
        (FF10,          RW10,           MINI_PLAYER),
        (MOVE_SCREEN_RIGHT,    MOVE_SCREEN_LEFT,      KC.RGB_TOG)
    )
]

if __name__ == '__main__':
    keyboard.go()

import sys
import time
import keyboard
from Xlib import display, X
from Xlib.ext import xtest

disp = display.Display()
root = disp.screen().root

def main():
    global disp
    global root
    autoclicker_active = False

    while not keyboard.is_pressed('escape'):
        if keyboard.is_pressed('ctrl'):
            autoclicker_active = True

        if autoclicker_active:
            autoclicker_logic(delay=0.01)
    sys.exit()

# 0.0 hold time = instant release
def autoclicker_logic(hold_time = 0.0, delay = 0.0):
    time.sleep(delay)
    xtest.fake_input(disp, X.ButtonPress, 1)
    disp.sync()
    time.sleep(hold_time)
    xtest.fake_input(disp, X.ButtonRelease, 1)
    disp.sync()

if __name__ == '__main__':
    main()
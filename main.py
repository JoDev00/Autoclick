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

    while not keyboard.is_pressed('escape'):
        autoclicker_logic(delay=1.0)
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
from pynput.keyboard import Key, Controller, Listener
import win32gui
keyboard = Controller()
Listener.daemon = False


def space(key):
    if "Discord" in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        if (key == Key.enter) or (key == Key.backspace) or (key == Key.delete):
            keyboard.press(key)
            keyboard.release(key)
            return False
        if (key == Key.shift) or (key == Key.caps_lock) or (key == Key.shift_r):
            return False
        keyboard.press(Key.space)
        keyboard.release(Key.space)
        return False


while True:
    with Listener(on_press=space) as listener:
        listener.join()


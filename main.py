import pyautogui
from random import randint
from pynput import keyboard

diff=70
x=870
y=530

cancel_key=keyboard.Key.esc
loot_key="-"

def on_press(key):
    if key == cancel_key:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k == loot_key:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        get_loot()

def get_loot():
    pyautogui.keyDown("alt")
    random_click(x-diff, y)
    random_click(x-diff, y-diff)
    random_click(x, y-diff)
    random_click(x+diff, y-diff)
    random_click(x+diff, y)
    random_click(x+diff, y+diff)
    random_click(x, y+diff)
    random_click(x-diff, y+diff)
    pyautogui.keyUp("alt")

def random_click(x, y):
    random_x = randint(0, 10) + x
    random_y = randint(0, 10) + y
    print(random_x, random_y)
    pyautogui.click(random_x, random_y)

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys

if __name__ == "__main__":
    main()
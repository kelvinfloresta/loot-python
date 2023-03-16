import pyautogui
import random 
import pynput
import time

diff=70
x=870
y=530

cancel_key=pynput.keyboard.Key.esc
loot_key="-"
help_key="="

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
    if k == help_key:
        print(pyautogui.position())

def get_loot():
    random_click(x-diff, y)
    random_click(x-diff, y-diff)
    random_click(x, y-diff)
    random_click(x+diff, y-diff)
    random_click(x+diff, y)
    random_click(x+diff, y+diff)
    random_click(x, y+diff)
    random_click(x-diff, y+diff)

def random_click(x, y):
    random_x = random.randint(0, 5) + x
    random_y = random.randint(0, 5) + y
    time.sleep(0.05)
    pyautogui.click(random_x, random_y, button="right")

def main():
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys

if __name__ == "__main__":
    main()
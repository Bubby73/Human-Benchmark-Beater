import pyautogui
import keyboard
import time
#print mouse position

while True:
    if keyboard.is_pressed('q'):
        print(pyautogui.position())
        time.sleep(0.2)

    if keyboard.is_pressed('esc'):
        break

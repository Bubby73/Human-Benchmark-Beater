from mss import mss
import mss.tools
import pyautogui
import keyboard
from PIL import Image
import time
import numpy as np

pyautogui.click(972, 418)

def click(white_pixel):
    screen_coordinate = (white_pixel[0], white_pixel[1] + monitor["top"])
    pyautogui.click(screen_coordinate[0], screen_coordinate[1])

for i in range (0, 30):
    with mss.mss() as sct:
        # The screen part to capture
        for i in range (0, 10):
            x = 500 + (i * 100)
            monitor = {"top": 200, "left": x, "width": 1, "height": 450}
            # Grab the data
            sct_img = sct.grab(monitor)

            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
            img_array = np.array(img)      

            white_pixel = None
            
            for y in range(img_array.shape[0]):
                if np.all(img_array[y] == [255, 255, 255]):
                    white_pixel = (x, y)
                    click(white_pixel)
                    break
                
                if white_pixel is not None:
                    pyautogui.moveTo(white_pixel[0], white_pixel[1])
                    break

    
                
                
        # convert white pixel coordinate to screen coordinate
        

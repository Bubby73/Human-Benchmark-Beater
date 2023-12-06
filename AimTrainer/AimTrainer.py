from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time

time.sleep(2)

top = 300
left = 500
width = 1000
height = 400

pyautogui.click(972, 450)

for i in range(0, 25):
        x = 100 + left
        
        while x < width + left: 
            with mss.mss() as sct:

                line = {"top": top, "left": x, "width": 1, "height": height}

                sct_img = sct.grab(line)

                img = Image.new("RGB", sct_img.size)

                pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[::4])
                img.putdata(list(pixels))
            
                
                y = 0
                while y < height:
                    r = img.getpixel((0, y))[0]      
                    if r != 43:
                        pyautogui.click(x, y + top)
                        break  
                        
                    y += 55
            x += 100

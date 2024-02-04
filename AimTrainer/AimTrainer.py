from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time

time.sleep(2)

top = 130
left = 855
width = 220
height = 100

pyautogui.click(972, 180)

for i in range(0, 25):
        x = 25 + left
        
        while x < width + left: 
            with mss.mss() as sct:

                line = {"top": top, "left": x, "width": 1, "height": height}

                sct_img = sct.grab(line)

                img = Image.new("RGB", sct_img.size)

                pixels = zip(sct_img.raw[2::4], sct_img.raw[1::4], sct_img.raw[::4])
                img.putdata(list(pixels))
                #time.sleep(0.2)
                
                y = 0
                while y < height:
                    #print(y)
                    #if x == 1100:
                        #img.show()
                    r = img.getpixel((0, y))[0]      
                    if r != 43:
                        pyautogui.click(x, y + top)
                        break  
                        
                    #y = height mod 10
                    y = 1 + y
            x += 25

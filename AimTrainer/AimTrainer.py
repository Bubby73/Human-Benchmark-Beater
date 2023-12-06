from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time
import numpy as np

time.sleep(2)

top = 300
left = 500
width = 1000
height = 400

pyautogui.click(972, 450)


for i in range (0, 30):    
        x = 100 + left
        
        while x < width + left: 
            with mss.mss() as sct:

                line = {"top": top, "left": x, "width": 1, "height": height}

                output = "line.png".format(**line)

                sct_img = sct.grab(line)

                y = 0
                while y < height:
                    pyautogui.moveTo(x + top, y + left)
                    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
                    im = Image.open("line.png")
                    rgb_im = im.convert('RGB')
                    r, g, b = rgb_im.getpixel((0, 0))
                    if g == 43:
                        #pyautogui.click(x, y)
                        print(x, y)
                        break  
                    
                

               
                    y += 2
            x += 100
            
    
                
                
  
        

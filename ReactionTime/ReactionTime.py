from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time

clicked = False

time.sleep(5)

pyautogui.click(970, 460)

while True:
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 400, "left": 960, "width": 1, "height": 1}
        output = "pxl.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)



    #check color of pixel

    im = Image.open("pxl.png")
    rgb_im = im.convert('RGB')
    r, g, b = rgb_im.getpixel((0, 0)) 
    # make rgb one variable
    print(r,g,b)

    if g == 38 and clicked == True:
        print ("red")
        clicked = False
          

    if g == 219 and clicked == False:
        #pyautogui.moveTo(970, 460) 
        pyautogui.click(970, 460)
        pyautogui.click(970, 460)
        clicked = True
        print ("green")
    

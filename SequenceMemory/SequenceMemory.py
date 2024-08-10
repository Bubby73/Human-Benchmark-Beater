from mss import mss
import mss.tools
import pyautogui
import keyboard
from PIL import Image
import time

mousePos = [[830,330],[960,330],[1090,330],[830,470],[960,470],[1090,470],[830,590],[960,590],[1090,590]]
pxlPos = [[65,90],[235,90],[400,90],[65,250],[235,250],[400,250],[65,410],[235,410],[400,410]]

sequence = []

time.sleep(3)

pyautogui.click(960, 570)

def screenShot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 240, "left": 730, "width": 460, "height": 460}
        output = "3x3.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)



    #check which square is white
    for j in range(0,9):
        im = Image.open("3x3.png")
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((pxlPos[j][0], pxlPos[j][1])) 
        # make rgb one variable
        if r == 255 and g == 255 and b == 255:
            return j
        
    return 9
    
def click():
    for i in range(0,len(sequence)):
        #time.sleep(0.1) 
        pyautogui.click(mousePos[sequence[i]][0], mousePos[sequence[i]][1])
        print(sequence[i])


level = 1
while True:
    if len(sequence) > 0:
        print(sequence)
    if len(sequence) < level:
        j = screenShot()
        if j != 9:
            if len(sequence) == 0:
                sequence.append(j)
            elif j != sequence[len(sequence)-1]:
                sequence.append(j)
            
                
    else:
        time.sleep(0.5)
        click()
        sequence = []
        
        level += 1

    #check if escape is pressed
    if keyboard.is_pressed('esc'):
        break









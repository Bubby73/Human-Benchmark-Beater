from mss import mss
import mss.tools
import pyautogui
import keyboard
from PIL import Image
import time

boundCoords = [[740, 330], [1210, 330], [740, 800], [1210, 800]]

time.sleep(2)

pyautogui.click(960, 570)


def screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 255, "left": 750, "width": 420, "height": 420}
        output = "VMSquare.png".format(**monitor)
    
        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

def numberOfsquares():
    screenshot()
    im = Image.open("VMSquare.png")
    rgb_im = im.convert('RGB')
    count = 0
    prev = False
    for x in range(0, 420):
        #pyautogui.moveTo(x + 750, 280)
        #if pixel is blue and previous pixel is not blue
        if rgb_im.getpixel((x, 25)) == (43, 135, 209) and prev == False:
            print("hallo")
            count += 1
            prev = True
            #print(count)
        if rgb_im.getpixel((x, 25)) != (43, 135, 209):
            prev = False

    print(count)
    return count
 

def findWhitesquares(gridSize):
    im = Image.open("VMSquare.png")
    rgb_im = im.convert('RGB')
    x =  420/gridSize/2
    y =  420/gridSize/2
    whiteSquares = []
    time.sleep(0.8)
    while x < 420:
        while y < 420:
            if rgb_im.getpixel((x, y)) == (255, 255, 255):
                whiteSquares.append((x, y))
                pyautogui.click(x + 740, y + 245)
            y = y + 420/gridSize
        x = x + 420/gridSize
        y = 420/gridSize/2
    
    return whiteSquares

time.sleep(0.6)
while True:
    time.sleep(0.6)
    screenshot()
    gridSize = numberOfsquares()
    gridSize -= 1
    whiteSquares = findWhitesquares(gridSize)


from mss import mss
import mss.tools
import pyautogui
import keyboard
from PIL import Image
import time

boundCoords = [[740, 330], [1210, 330], [740, 800], [1210, 800]]

time.sleep(5)

pyautogui.click(980, 670)


def screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 335, "left": 740, "width": 520, "height": 470}
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
    firstSquare = 0
    for x in range(0, 470):
        #if pixel is blue and previous pixel is not blue
        if rgb_im.getpixel((x, 10)) == (43, 135, 209) and prev == False:
            count += 1
            prev = True
        if rgb_im.getpixel((x, 10)) != (43, 135, 209):
            prev = False

    return count
 

def findWhitesquares(gridSize):
    im = Image.open("VMSquare.png")
    rgb_im = im.convert('RGB')
    x =  470/gridSize/2
    y =  470/gridSize/2
    whiteSquares = []
    print(x, y)
    time.sleep(0.8)
    while x < 470:
        while y < 480:
            if rgb_im.getpixel((x, y)) == (255, 255, 255):
                whiteSquares.append((x, y))
                pyautogui.click(x + 740, y + 330)
            y = y + 470/gridSize
        x = x + 470/gridSize
        y = 470/gridSize/2
    
    print(whiteSquares)
    return whiteSquares

time.sleep(0.6)
while True:
    time.sleep(0.6)
    screenshot()
    gridSize = numberOfsquares()
    gridSize += 1
    whiteSquares = findWhitesquares(gridSize)


from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time
import easyocr
from pynput.keyboard import Key, Controller


time.sleep(3)

pyautogui.click(960, 600)


def screenshot(left, width):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 370, "left": left, "width": width, "height": 110}
        output = "numberMem.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)


def findPixel():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 430, "left": 510, "width": 1, "height": 1}
        output = "memPxl.png".format(**monitor)
        # Grab the data
        sct_img = sct.grab(monitor)
        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        im = Image.open("memPxl.png")
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((0, 0)) 

        if r == 34 and g == 108 and b == 187:
            return 1
        else:
            return 0

def detectNumber():
    #image = Image.open('chimp.png')
    #new_image = image.resize((500, 500))
    #new_image.save('chimp.png')


    reader = easyocr.Reader(['en'])
    results = reader.readtext('numberMem.png')

    detected_numbers = [result[1] for result in results]

    # If you're expecting only one number per image, you can use:
    detected_number = detected_numbers[0] if detected_numbers else None

    return detected_number

time.sleep(0.2)

left = 898
width = 125
score = 0

while True:
    if width < 1870:
        screenshot((left - (score * 25)), (width + (score * 50)))
    else:
        screenshot((0), (1920))

    number = detectNumber()
    print(number)

    time.sleep(2)

    while findPixel() == 0:
        time.sleep

    #type in the number
    keyboard = Controller()
    for char in number:
        keyboard.press(char)
        keyboard.release(char)

    #press enter
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(0.2)

    score += 1


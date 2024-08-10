from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time
import easyocr

top = 205
left = 600
width = 90 * 8
height = 90 * 5

path = []

time.sleep(2)

pyautogui.click(960, 570)

def coordsCalctop(y):
    top = 205 + (90 * y)
    return top

def coordsCalcleft(x):
    left = 600 + (90 * x)
    return left


def screenShot(x, y):
    with mss.mss() as sct:
        # The screen part to capture
        top = coordsCalctop(y)
        left = coordsCalcleft(x)
        monitor = {"top": (top), "left": (left), "width": 90, "height": 90}

        pyautogui.moveTo(left, top)

        output = "chimp.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        
        im = Image.open("chimp.png")
        rgb_im = im.convert('RGB')
        for i in range(5, 85):
            r, g, b = rgb_im.getpixel((i, 45)) 
            if r == 255 and g == 255 and b == 255:
                return 1
        return 0


screenShot(3, 4)


def detectNumber():
    #image = Image.open('chimp.png')
    #new_image = image.resize((500, 500))
    #new_image.save('chimp.png')


    reader = easyocr.Reader(['en'])
    results = reader.readtext('chimp.png')

    detected_numbers = [result[1] for result in results]

    # If you're expecting only one number per image, you can use:
    detected_number = detected_numbers[0] if detected_numbers else None

    return detected_number

level = 0
while level < 1:
    x = 0
    y = 0
    while y <= 4:
        while x <= 7:
            if screenShot(x, y) == 1:
                number = detectNumber()
                path.append([int(number), [x, y]])
                print(path)

            x += 1

        y += 1
        x = 0

    sortedPath = sorted(path, key=lambda x: x[0])
    print(sortedPath)
    
    j = 0
    while j < len(sortedPath):
        pyautogui.click(((coordsCalcleft(sortedPath[j][1][0])) + 45),  ((coordsCalctop(sortedPath[j][1][1])) + 45))
        j += 1
        #time.sleep(0.2)

    path = []
    sortedPath = []
    pyautogui.click(960, 570)
    level += 1
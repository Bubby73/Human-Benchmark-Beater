from mss import mss
import mss.tools
import pyautogui
from PIL import Image
import time
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

def screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 375, "left": 700, "width": 550, "height": 110}
        output = "wordMem.png".format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture specific file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

pyautogui.click(960, 600)

words = []
#time.sleep(0.2)
while True:
    screenshot()
    word = pytesseract.image_to_string(Image.open('wordMem.png'), lang='eng')
    print(word)
    if word in words:
        pyautogui.click(890, 510)
    
    else:
        words.append(word)
        pyautogui.click(1030, 510)
         
        
import pyautogui
from PIL import ImageGrab

def grabImg(pos1X, pos1Y, pos2X, pos2Y, saveLoc, fileName):
    img=ImageGrab.grab(bbox=(pos1X,pos1Y,pos2X,pos2Y), all_screens=True)
    saveas= saveLoc + '/' + fileName
    img.save(saveas)
    # pyautogui.screenshot(fileName, (pos1X, pos1Y, pos2X, pos2Y))
import pyautogui
import mouse
import time

def returnMousePos():
    # print("Mouse clicked at: ", pyautogui.position())
    # return (pyautogui.position().x, pyautogui.position().y)
    time.sleep(0.05)
    while(True):
        if mouse.is_pressed("left"):
            print("Mouse clicked at: ", pyautogui.position())
            return (pyautogui.position().x, pyautogui.position().y)

def mouseClick(posX, posY):
    pyautogui.moveTo(posX, posY)    # move mouse
    pyautogui.click(button="left")  # click mouse
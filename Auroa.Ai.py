import os

import pyautogui
import time

time.sleep(5)

user_input = str(input("Type 'Forward' or 'Backward' to move: "))
while True:
    if user_input.lower() == "forward":
        pyautogui.keyDown("w")
        time.sleep(1)
        pyautogui.keyUp("w")
    elif user_input.lower() == "backward":
        pyautogui.keyDown("s")
        time.sleep(1)
        pyautogui.keyUp("s")

    elif user_input.lower() == "left":
        pyautogui.keyDown("a")
        time.sleep(1)
        pyautogui.keyUp("a")

    elif user_input.lower() == "right":
        pyautogui.keyDown("d")
        time.sleep(1)
        pyautogui.keyUp("d")
    elif user_input.lower() == "Auto clicker":
        os.startfile(r"C:\Users\rahul\Downloads\AutoClicker-3.0 (1).exe")
        pyautogui.keyDown("b")
        time.sleep(0.5)
        pyautogui.keyUp("b")

    elif user_input.lower() == "Menu":
        pyautogui.moveTo(91,706)
        pyautogui.click()




    else:
        print("Invalid input. Please type 'Forward' or 'Backward'.")

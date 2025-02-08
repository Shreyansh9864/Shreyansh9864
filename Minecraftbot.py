import pyautogui
import warnings
import time
pyautogui.moveTo( 213,1051)
pyautogui.click()
pyautogui.moveTo(389, 375)
pyautogui.click()
pyautogui.moveTo(464, 853)
pyautogui.click()
time.sleep(10)
pyautogui.moveTo(868, 1051)
pyautogui.click()
pyautogui.moveTo(  953, 596)
pyautogui.click()
pyautogui.moveTo(904, 839)
pyautogui.click()
pyautogui.typewrite("TestExds.aternos.me:12350")
time.sleep(0.5)
pyautogui.press("enter")
while True:
    user = input("Type to move:")
    if user.lower() == "Forward":
        pyautogui.keyDown("w")
        time.sleep(5)
        pyautogui.keyUp("w")
    elif user.lower() == "Backward":
        pyautogui.keyDown("s")
        time.sleep(5)
        pyautogui.keyUp("s")
    elif user.lower() == "right":
        pyautogui.keyDown("a")
        time.sleep(5)
        pyautogui.keyUp("a")
    elif user.lower() == "Left":
        pyautogui.keyDown("d")
        time.sleep(5)
        pyautogui.keyUp("d")

    elif user.lower() == "Hit":
        pyautogui.leftClick()
        time.sleep(5)

   elif user.lower() == "Place":
        pyautogui.Rightclick()
        time.sleep(5)

    elif user.lower() =="Jump":
        pyautogui.keyDown("spacebar")
        time.sleep(1)
        pyautogui.keyUp("Spacebar")
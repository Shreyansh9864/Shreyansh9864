import openai
import webbrowser
import datetime
from openai import OpenAI
import PyPDF2
import smtplib
import pywhatkit as py
import os
import speechreocnization
import pyautogui
import pyttsx4
import cv2
import time


client_openai = OpenAI(api_key="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")

while True:
    user_input = input("Type to chat: ")

    if "generate image" in user_input.lower():
        user_prompt = input("Type to generate image: ")
        response = client_openai.images.generate(
            model="dall-e-3",
            prompt=user_prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        print(image_url)
        webbrowser.open(image_url)

    elif "time" in user_input.lower():
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current Time =", current_time)

    elif "date" in user_input.lower():
        today = datetime.date.today()
        print("Today's date:", today)

    elif "year" in user_input.lower():
        year = datetime.date.today().year
        print("Current Year:", year)

    elif "month" in user_input.lower():
        month = datetime.date.today().strftime("%B")
        print("Current Month:", month)

    elif "read pdf" in user_input.lower():
        with open("Example.pdf", "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text = page.extract_text()
                print(text)

    elif "email" in user_input.lower():
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        user_email = input("Enter your email: ")
        password = input("Enter your password: ")
        receiver_email = input("Enter receiver's email: ")
        message = input("Type your message: ")
        server.login(user_email, password)
        server.sendmail(user_email, receiver_email, message)
        server.quit()

    elif "play music" in user_input.lower() or "play video" in user_input.lower():
        video_name = input("Enter video name: ")
        py.playonyt(video_name)

    elif "increase volume" in user_input.lower():
        pyautogui.press("volumeup")

    elif "decrease volume" in user_input.lower():
        pyautogui.press("volumedown")

    elif "type" in user_input.lower():
        text_to_type = input("Enter text to type: ")
        pyautogui.typewrite(text_to_type)

    elif "screenshot" in user_input.lower():
        print("Taking screenshot, switch to desired window...")
        time.sleep(3)
        screenshot = pyautogui.screenshot()
        filename = str(time.time()) + ".png"
        screenshot.save(filename)
        print("Screenshot saved as", filename)

    elif "open opera" in user_input.lower():
        os.startfile(r"C:\Users\rahul\AppData\Local\Programs\Opera GX\launcher.exe")

    elif "close opera" in user_input.lower():
        os.system("taskkill /f /im launcher.exe")

    elif "open pycharm" in user_input.lower():
        os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.3.2\bin\pycharm64.exe")

    elif "close pycharm" in user_input.lower():
        os.system("taskkill /f /im pycharm64.exe")

    elif "open discord" in user_input.lower():
        os.startfile(r"C:\Users\rahul\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")

    elif "close discord" in user_input.lower():
        os.system("taskkill /f /im discord.exe")

    elif "open vscode" in user_input.lower():
        os.startfile(r"C:\Users\rahul\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    elif "close vscode" in user_input.lower():
        os.system("taskkill /f /im Code.exe")

    elif "open cmd" in user_input.lower():
        os.system("start cmd")

    elif "close cmd" in user_input.lower():
        os.system("taskkill /f /im cmd.exe")

    elif "open app" in user_input.lower():
        app_name = input("Enter the app name: ")
        os.startfile(app_name)

    elif "close app" in user_input.lower():
        app_name = input("Enter the app name to close: ")
        os.system(f"taskkill /f /im {app_name}.exe")


    else:
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )
        print(completion.choices[0].message.content)

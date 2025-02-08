import requests as r
import openai
import webbrowser
import datetime
from openai import OpenAI
import PyPDF2
import smtplib
import pywhatkit as py
import os
import wolframalpha
import pyautogui
import cv2
import time as t
import socket
import re

from newsapi import newsapi_client
import pyttsx3
import random
import wikipedia
from googletrans import Translator
from termcolor import colored
import webbrowser
import pywhatkit as py
import wolframalpha
import os
news_api = newsdataapi_client(api_key ="456e827c351341498fe3e260347542b3")
client_openai = OpenAI(api_key="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")
client = wolframalpha.Client("6V4P66-L5TKY4Y3EJ")
weather_api_key ="7cb6ee346809341622c64006cc717d98"
def get_news_api(news):
    response = news_api.news_api()


    print("Login")
time.sleep(0.7)
login = input('Sign up if you are new or Login if you have made your account: ')

if login == "Sign up":
    name = input("Tell your user name: ")
    password = input("Tell your password: ")
    password2 = input("Tell your password to conform: ")

    if password == password2:
        print("Success")
        with open("login.txt", "w") as f:
            f.write(f"Name = {name}, password = {password}")
    else:
        print("Invalid")

elif login == "Log in":
    with open("login.txt", "r") as read:
        n = input("Enter user name: ")
        p = input("Enter password: ")
        for lines in read:
            if re.match(n, p):
                print("Successfully logged in")

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
        with open(r"C:\Users\rahul\Downloads\CMH_Pub_72-2.pdf", "rb") as file:
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
        time.sleep(2)
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

    elif "record" in user_input.lower():
        cap = cv2.VideoCapture(0)

        while True:
            success, record = cap.read()
            cv2.imshow("Webcam", record)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    elif "location" in user_input:
        try:
            res = client.query("my location")
            output = next(res.results).text

            print(output)
        except Exception as e:
            print("error")

    elif "weather" in user_input:
        try:
            res = client.query("How is the weather today")
            output = next(res.results).text

            print(output)
        except Exception as e:
            print("error")

    elif "ip address" in user_input:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)

        print("Your Computer Name is:" + hostname)
        print("Your Computer IP Address is:" + IPAddr)

    elif "sleep" in user_input:
        print("Thank you for using me")
        break

    elif "What is your name" in user_input:
        print("My name is Raj")

    elif "what is my name" in user_input:
        print(f"Your name is {name}")

    elif news in user_input:
        get_news_api()
        print(response)

    elif wheater2 in user_input:
        weather = input("Enter city :")
        wather_data =r.request(
       f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
        )
    if weather_data == 404:
        print("no city found")
    # Here is the brain code
    engine = pyttsx3.init()
    translator = Translator()
    engine.setProperty("rate", 180)
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    # Key
    client = wolframalpha.Client('6V4P66-URL2LA4PQ3')

    engine.say("Hi, I am an AI assistant, and my name is Krishna")
    print(colored("Hi, I am an AI assistant, and my name is Krishna", "cyan"))
    engine.runAndWait()
    name = str(input("Enter ur name:"))
    engine.say("Enter ur name")
    engine.runAndWait()
    print("Nice to meet u  " + name)
    engine.say("Nice to meet u" + name)
    engine.runAndWait()

    engine.say("Please type /help for a list of programs")
    print(colored("Please type /help for a list of all programs", "red", on_color="on_white"))
    engine.runAndWait()

    user1 = input("Type /help for a list of programs:")
    help_programs = [
        "Open Calculator, Start Calculator - Calculator",
        "Jokes - listen to jokes",
        "Open Translator, Start Translator - Translation",
        "Search or Search2 - find information",
        "Riddles - get riddles",
        "chat - to chat",
        "open opera or open vscode"
    ]
    print(colored(help_programs, "cyan"))
    engine.say(str(help_programs))  # Fix: Converted help_programs to string
    engine.runAndWait()

    # Here is the jokes code
    jokes = [
        "What falls but never needs a bandage? The rain.",
        "I was going to tell you a joke about boxing but I forgot the punch line.",
        "I'm not a fan of spring cleaning. Let's be honest, I'm not into summer, fall, or winter cleaning either.",
        "Why did the egg hide? It was a little chicken.",
        "What did the dirt say to the rain? If you keep this up, my name will be mud.",
        "Why couldn't the sunflower ride its bike? It lost its petals.",
        "What's an egg's favorite vacation spot? New Yolk City.",
        "I ate a sock yesterday. It was very time-consuming.",
        "What kind of candy do astronauts like? Mars bars.",
        "I wanted to buy some camo pants but couldn't find any.",
        "I ordered a chicken and an egg from Amazon. I'll let you know.",
        "What month is the shortest of the year? May, it only has three letters.",
        "What did the snail who was riding on the turtle's back say? Wheeeee!",
        "I was going to tell a time traveling joke, but you guys didn't like it.",
        "What do you call a lazy kangaroo? A pouch potato.",
        "I used to run a dating service for chickens, but I was struggling to make hens meet.",
        "Why do we tell actors to 'break a leg?' Because every play has a cast.",
        "What does a pig put on dry skin? Oinkment.",
    ]

    # Here is the riddle code
    riddles = [
        "Riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?\nAnswer: An Echo.",
        "Riddle: The more you take, the more you leave behind. What am I?\nAnswer: Footsteps.",
        "Riddle: I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?\nAnswer: Pencil lead/graphite.",
        "Riddle: The person who makes it, sells it. The person who buys it never uses it. What is it?\nAnswer: Coffin.",
        "Riddle: The more you look at it, the less you see. What is it?\nAnswer: Darkness.",
        "Riddle: I have keys but no locks. I have space but no room. You can enter, but you can't go inside. What am I?\nAnswer: Keyboard.",
        "Riddle: The one who makes it, sells it. The one who buys it never uses it. The one who uses it never knows they're using it. What is it?\nAnswer: Coffin.",
        "Riddle: The more you take, the more you leave behind. What am I?\nAnswer: Footsteps.",
        "Riddle: I can be cracked, made, told, and played. What am I?\nAnswer: A Joke.",
        "Riddle: The person who makes it, sells it. The person who buys it never uses it. The person who uses it never knows they're using it. What is it?\nAnswer: Coffin.",
    ]

    # Here the loop starts
    while True:
        user = input("Queries: ")

        # Here the jokes code work
        if user.lower() in ["joke", "jokes"]:
            r_jokes = random.choice(jokes)
            print(colored(r_jokes, "yellow"))
            engine.say(r_jokes)
            engine.runAndWait()

        # Here the calculator program
        elif user.lower() in ["33", "start calculator", "calculator"]:
            x = eval(input("Enter the digits: "))
            engine.say(x)
            print(x)
            engine.runAndWait()

        # Here the translator code works, but translation does not happen
        elif user.lower() in ["start translator", "open translator", "translator"]:
            try:
                # Here the translator code works, but translation does not happen
                x = input("Type a word in any language: ")
                languages = '''
                hi: Hindi
                ta: Tamil
                es: Spanish
                fr: French
                ja: Japanese
                ta:telgu
                en:english
                be:bengali
                '''
                print(colored("Supported languages:", "cyan"))
                print(colored(languages, "cyan"))
                y = input("Translate to which language (use language code): ")

                # Perform translation
                result = translator.translate(x, dest=y)

                # Print the translated text
                print(colored("Translated text:", "cyan"))
                print(colored(result.text, "cyan"))

                # Speak the translated text
                engine.say(result.text)
                engine.runAndWait()

            except Exception as e:
                print(colored(f"Error: {e}", "red"))


        # Here the search happens
        elif user.lower() == "search":
            try:
                a = input("Type what do you want to search about: ")
                b = wikipedia.summary(a, sentences=2)
                print(colored(b, "cyan"))
                engine.say(b)
                engine.runAndWait()
            except wikipedia.exceptions.DisambiguationError as e:
                print(colored("Invalid ", "red", on_color="on_black"))
                engine.say("Invalid ")
                engine.runAndWait()

        # Here the bye code
        elif user.lower() in ["bye bye", "bye", "tata", "good bye"]:
            print(colored("Bye bye", "cyan"))
            engine.say("Bye BYe")
            engine.runAndWait()
            break

        # Here the creator code
        elif user.lower() in ["who made u", "who made you"]:
            print(colored("It was made by Shreyansh And Rohit sir help and other question.", "white", "on_blue"))
            engine.say("It was made by Shreyansh And Rohit sir help and other question.")
            engine.runAndWait()

        # Here the preethi ma'am
        elif user.lower() == "who is the class teacher of c4c":
            print(colored("Preethi Ma'am is the class teacher of C4C and nice to ask.", "green", "on_yellow"))
            engine.say("Preethi Ma'am is the class teacher of C4C and nice to ask")
            engine.runAndWait()

        # Here the riddles code is here+++-----------
        elif user.lower() == "what are the riddles":
            r_riddles = random.choice(riddles)
            print(colored(r_riddles, "cyan"))
            engine.say(r_riddles)
            engine.runAndWait()

        elif user.lower() in ["how are u", "hi, ai! how are you today?"]:
            print("Hello, nice to ask. Same to you!")
            engine.say("Hello, nice to ask. Same to you!")
            engine.runAndWait()

        elif user.lower() == "what ur name":
            print("My name is Krishna.")
            engine.say("My name is Krishna")
            engine.runAndWait()

        elif user.lower() == "what's your favorite color":
            print("Red is my favorite color.")
            engine.say("Red is my favorite color")
            engine.runAndWait()

        elif user.lower() == "what are ur hobby":
            print("Playing music is my hobby.")
            engine.say("Playing music is my hobby")
            engine.runAndWait()

        elif user.lower() == "tell me ur favrarate song":
            print("Faded is my favorite song. Nice to ask!")
            engine.runAndWait()

        elif user.lower() == "what is ur fav food":
            print("I am a computer, I have no favorite food.")
            engine.say("I am a computer, I don't have a favorite food")
            engine.runAndWait()

        elif user.lower() == "were wereu made":
            print("I was made in India, Bangalore.")
            engine.say("I was made in India, Bangluru")
            engine.runAndWait()

        elif user.lower() == "who is ur teacher" or user.lower() == "who is your teacher":
            print("Rohit sir is my favorite teacher.")
            engine.say("Rohit sir is my favorite sir")
            engine.runAndWait()

        elif user.lower() == "search2":
            print("I am gonna search:")
            x = input()
            engine.say("I'm gonna search for you")
            engine.runAndWait()
            print("Now opening")
            engine.say("Now opening")
            engine.runAndWait()
            webbrowser.open("https://www.google.com/search?q=" + x)

        elif user.lower() == "search video":
            user2 = input("Enter the video you want to search:")
            engine.say("Searching for video")
            engine.runAndWait()
            print("Now opening")
            engine.say("Now opening")
            engine.runAndWait()
            py.playonyt(user2)

        elif user.lower() == "chat":
            try:
                user_input = str(input("Enter something to chat:"))
                res = client.query(user_input)
                output = next(res.results).text
                engine.say(output)
                engine.runAndWait()
                print(output)

            except Exception as e:
                print(f"Error: {e}")

        elif user.lower() == "open opera":
            os.startfile(r"C:\Users\rahul\AppData\Local\Programs\Opera GX\launcher.exe")

        elif user.lower() == "open vscode":
            os.startfile(r"C:\Users\rahul\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif user.lower() == "ttv":
            tts = str(input("Type a word to make me say"))
            engine.say(tts)
            engine.runAndWait()
        elif user.lower() == "Open google":
            wb.open("www.google.com")
        elif user.lower() == "Open yutube":
            wb.open("www.yotube.com")
        elif user.lower() == "Open Instartgram":
            wb.open("www.instragram.com")
        elif user.lower() == "Open Twitter":
            wb.open("www.twitter.com")
        elif user.lower() == "Open app":
            s = input("App name:")
            wb.open(s)
        elif user.lower() == "Close app":
            z = input("app name to close:")
            wb.close(s)



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












































    join
    this



# import pyautogui
# import pyautogui as pgi
# import time
# pyautogui.FAILSAFE = False
# time.sleep(0.7)
# while True:
#     pgi.click(clicks=100000000000000000000000000, interval=0.000001)
# from google.generativeai import generative_models as genai
# apikey="AIzaSyCTQPsTCoSEttmuf9JnFIysKHy2d0OfcUM"
# google_api = genai(apikey=apikey)
# model = genai.generative_modelsmodels('gemni-pro')
# conent = model.generate_content("What is 2 +2")
# print(conent.txt)
# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key

GOOGLE_API_KEY = "AIzaSyCTQPsTCoSEttmuf9JnFIysKHy2d0OfcUM"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
#
# while True:
#     user = input("User:")
#     response = model.generate_content(user)
#     messages = [
#         {'role': 'user',
#          'parts': user,}
#     ]
#     response = model.generate_content(messages)
#
# #     print(f"User {user}")
#     print("Bot:",response.text)
user = input()
chat = model.start_chat(history =[])
def get_gemni_respponse(user):
    response = chat.send_message(user,stream=True)
    return response

# response = chat.send_message("What is meaning of life")
# print(response.text)
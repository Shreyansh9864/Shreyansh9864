from openai import OpenAI
api_key = "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"
# key = OpenAI(api_key=api_key)
# OpenAI.chat.completions.create(
#
#
# )

# Use a pipeline as a high-level helper
# Use a pipeline as a high-level helper
# from transformers import pipeline
#
# pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
#
#
# # Load model directly
# from transformers import AutoTokenizer, AutoModelForSequenceClassification
#
# tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment-latest")


# 
# 
# # ment-latest")
# from langchain_openai import ChatOpenAI
# from langchain_openai import OpenAI
# 
# llm = OpenAI()
# chat_model = ChatOpenAI(model="gpt-4")
# 
# llm = ChatOpenAI(openai_api_key=api_key)
# chat_model = ChatOpenAI(model="gpt-4")
# user = input("User:")
# 
# bot = llm.invoke(user)
# print(user[0])
# print(f"User:{user}")
# print(f"Bot:{bot}")
import google.generativeai as genai
# genai.configure(api_key="AIzaSyAiJCdYTQxsOokxnMaBtnkbBHB8iFQWO5A")
# # for m in genai.list_models():
# #   if 'generateContent' in m.supported_generation_methods:
# #     print(m.name)
# model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
# response = model.generate_content("What is the meaning of life?")
# print(response)
from langchain_openai import OpenAI
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate as cpt
# user = input("YpeZ:")
# prompt =  cpt(
# input_var = ["funny","scarry"],
# templete = "Tell me a story with {funny},{scarry}",
# )
# tempelete ="Tell me stroy with {funny},{scarry}"
# helper_prompt = cpt.from_template(tempelete)
#
#
#
# key = OpenAI(api_key="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")
# chain = prompt | key
# bot =key.invoke('What is the meaning of life')
# x =chain.invoke({"input": "how can langsmith help with testing?"})
# print( x)

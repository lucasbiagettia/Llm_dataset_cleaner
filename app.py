import os

from groq_client import Chatbot
from promt_provider import PromptProvider

groq_api_key = os.getenv("GROQ_API_KEY")
prompt_string = input("Insert instructions to clean the dataset")
prompt = PromptProvider(prompt_string)

chatbot = Chatbot(api_key= groq_api_key, prompt_provider= prompt)

data_to_clean = input("Insert data to clean")

clean_data = chatbot.make_request(data_to_clean)

print (clean_data)
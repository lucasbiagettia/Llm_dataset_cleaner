import json
import os
import time
import xml.etree.ElementTree as ET
from groq_client import Chatbot
from pdf_extractor import PdfExtractor
from promt_factory import PromptFactory

groq_api_key = os.getenv("GROQ_API_KEY")
prompt_factory = PromptFactory()
prompt = prompt_factory.get_question_generator_prompt()
chatbot = Chatbot(api_key= groq_api_key, prompt= prompt)

pdf_extractor = PdfExtractor()



def process_folder(folder_path, use_free_groq_api_key=True):
    processed_files = {}
    for filename in os.listdir(folder_path):
        try:
            if filename.endswith('.pdf'):
                file_path = os.path.join(folder_path, filename)
                proccessed = process_file(file_path, use_free_groq_api_key)
                processed_files[filename]= proccessed
        except Exception as e:
            print(e)
            
        if use_free_groq_api_key:
            time.sleep(80) #Free groq api key limit is 1 requests per minute  

    return processed_files


def process_file(file_path, use_free_groq_api_key):
    data = pdf_extractor.extract_text_from_pdf(file_path)
    if use_free_groq_api_key:
        short_data = data[:80000] #Limit, arround 20000 tokens (groq limitation is arround 30000)
        questions = generate_questions(short_data)
    else:
        questions = generate_questions(data)
    dict = {"questions": questions, "data": data}
    return dict


def generate_questions(data):
    
    xml_questions = chatbot.make_request(data)

    root = ET.fromstring(xml_questions)

    questions = []

    for child in root:
        questions.append(child.text)
      

    return questions

folder_path = 'data'
processed_files = process_folder(folder_path)


with open("processed_files.json", 'w') as json_file:
    json.dump(processed_files, json_file)
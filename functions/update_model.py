from functions.file_downloader import model_downloader
import requests
import time
from datetime import datetime

def update_model():
    with open('text_classification/model/updated_at.txt', 'r', encoding='utf-8') as file:
        updated_at = file.read()

    updated_at_github = requests.get('https://raw.githubusercontent.com/Polynomial232/Ringing-Recognition/dev/text_classification/model/updated_at.txt')

    if updated_at != str(updated_at_github.json()):
        model_downloader('https://raw.githubusercontent.com/Polynomial232/Ringing-Recognition/dev/text_classification/model/intents.json', 'intents.json')
        model_downloader('https://raw.githubusercontent.com/Polynomial232/Ringing-Recognition/dev/text_classification/model/data.pth', 'data.pth')
        print(f'{datetime.now()}\t model update done')
    else:
        print(f'{datetime.now()}\t model is already in the updated')

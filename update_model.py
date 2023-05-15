from functions.file_downloader import model_downloader
import requests

with open('text_classification/model/updated_at.txt', 'r', encoding='utf-8') as file:
    updated_at = file.read()

# model_downloader('https://raw.githubusercontent.com/Polynomial232/Ringing-Recognition/dev/text_classification/model/intents.json', 'intents.json')
# model_downloader('https://raw.githubusercontent.com/Polynomial232/Ringing-Recognition/dev/text_classification/model/data.pth', 'data.pth')

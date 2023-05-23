from text_classification.transcribe_audio import transcribe_audio
import os
import random

def main(filepath, filename):
    text = transcribe_audio(filepath, filename)

    with open('recognition.txt', 'a', encoding='utf-8') as file:
        file.write(text+'\n')

    print(text)

for i in range(10):
    filename = 't'
    main(f'{filename}.wav', filename)
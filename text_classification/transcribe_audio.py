"""
    docstring
"""

import os
import time

def transcribe_audio(path, filename):
    """
        docstring
    """

    # os.system(f"whisper {path} --language Indonesian --model base --output_format txt --fp16 False > /dev/null")
    os.system(f"whisper {path} --language Indonesian --model base --output_format txt --fp16 False > temp")
    with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines()

    os.system(f"whisper {path} --language English --model base --output_format txt --fp16 False > temp")
    with open(f'{filename}.txt', 'r', encoding='utf-8') as file:
        text = file.read().splitlines() + text
    
    return " ".join(text)

import os
import whisper
from whisper import model
# dirs = 'valid-online-trim'
# result = ''
# for filename in os.listdir(dirs):
#     # print(filename)
#     directory = dirs+'/'+filename
#     for file in os.listdir(directory):
#         if file.endswith(".wav"):
#             filepath = os.path.join(dirs, file)
#             outputFile = os.path.join(filename[:5]+'.txt')
#             model = whisper.load_model("medium")
#             text = model.transcribe(f'{directory}/{file}')
#             result = result + text.get('text')
#         with open(outputFile, 'w') as f:
#             f.write(result)
import subprocess
import re


async def transcribeBulkAudio():
    for filename in os.listdir('invalid'):
        output = subprocess.check_output(
            f"whisper valid-online/{filename} --language Indonesian --model base", shell=True)


def transcribeAudio(path):
    pattern = r'\[\d\d:\d\d\.\d+\s-->\s\d\d:\d\d\.\d+\]\s'
    output = subprocess.check_output(
        f"whisper {path} --language Indonesian --model base --output_format txt", shell=True)
    return re.sub(pattern, '', output.decode())

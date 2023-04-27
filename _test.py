"""
    docstring
"""
# pylint: disable=line-too-long, unused-import

import time
import os
from datetime import datetime
import shutil
import requests
import audio_metadata
from decouple import config
from mutagen.wave import WAVE
from ringing_detection import ringing_recognition
from file_downloader import file_downloader
from samplerate_conv import samplerate_conv


COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
PC_CODE = config("PC_CODE")

def main():
    """
        docstring
    """

    # file_path = "allowed.wav"
    file_path = "audio/62817865885_1682570895.005631.wav"
    file_path = samplerate_conv(file_path)
    # file_path = "audio/"+random.choice(os.listdir("audio"))
    
    # for i in os.listdir("audio"):
    #     if 'wav' not in i:
    #         continue
    #     print(i)

    #     file_path = "audio/"+i
    #     audio_info = WAVE(file_path).info

    #     if audio_info.length < 1:
    #         print(audio_info.length)
    #         # return
    #     elif audio_info.channels != 1:
    #         print(audio_info.channels)
    #         # return
    #     elif audio_info.sample_rate != 48_000:
    #         print(audio_info.sample_rate)
    #         # return
    
    text = transcribe_audio(file_path, "62817865885_1682570895.005631")
    print(text)
    # classes, status = ringing_recognition(file_path)
    # print(f"{datetime.now()}\t Status: {status}, Deskripsi: {classes}")

main()
# reset = True
# AUDIO_PATH = "audiob"
# while True:
#     if reset:
#         start = time.perf_counter()
#         reset = False

    # main()
#     time.sleep(COOLDOWN)

#     if (time.perf_counter() - start) >= 10:
#         shutil.rmtree(AUDIO_PATH)
#         os.makedirs(AUDIO_PATH, exist_ok=True)
#         reset = True
"""
    docstring
"""
# pylint: disable=line-too-long, unused-import

import time
import os
from datetime import datetime
import requests
from decouple import config
from ringing_detection import ringing_recognition
from file_downloader import file_downloader
from text_classification.transcribe_audio import transcribe_audio
import audio_metadata
import mutagen
from mutagen.wave import WAVE
import shutil

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
DEVICE_CODE = config("DEVICE_CODE")

# ISAT-6285815757134_185_6e3573e5_1681463743.2010014.wav

def main():
    """
        docstring
    """

    # file_path = "audio/ISAT-6285815254405_98_6ff593e5_1681463710.0353189.wav"
    # file_path = "audio/"+random.choice(os.listdir("audio"))
    
    for i in os.listdir("audio"):
        if 'wav' not in i:
            continue
        print(i)

        file_path = "audio/"+i
        audio_info = WAVE(file_path).info

        if audio_info.length < 1:
            print(audio_info.length)
            # return
        elif audio_info.channels != 1:
            print(audio_info.channels)
            # return
        elif audio_info.sample_rate != 48_000:
            print(audio_info.sample_rate)
            # return
    

    # classes, status = ringing_recognition(file_path)
    # print(f"{datetime.now()}\t Status: {status}, Deskripsi: {classes}")

# main()

reset = True
AUDIO_PATH = "audiob"
while True:
    if reset:
        start = time.perf_counter()
        reset = False

    # main()
    time.sleep(COOLDOWN)

    if (time.perf_counter() - start) >= 10:
        shutil.rmtree(AUDIO_PATH)
        os.makedirs(AUDIO_PATH, exist_ok=True)
        reset = True
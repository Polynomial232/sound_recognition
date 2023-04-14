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

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
DEVICE_CODE = config("DEVICE_CODE")

# ISAT-6285815757134_185_6e3573e5_1681463743.2010014.wav

def main():
    """
        docstring
    """

    file_path = "audio/ISAT-6285815254405_98_6ff593e5_1681463710.0353189.wav"
    classes, status = ringing_recognition(file_path)
    print(f"{datetime.now()}\t Status: {status}, Deskripsi: {classes}")

main()

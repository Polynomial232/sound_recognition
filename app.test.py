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
from functions.file_downloader import file_downloader
from functions.samplerate_conv import samplerate_conv
from text_classification import transcribe_audio
import random

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
PC_CODE = config("PC_CODE")

def validate_audio(file_path, filename, result_id, msisdn, device_code):
    """
        Mengecek apakah audio sudah sesuai standar atau belum
        durasi audio tidak boleh 0
        channels audio 1
        sample rate 48_000 Hz
    """

    classes = ""
    status = 3

    audio_info = WAVE(file_path).info

    if audio_info.length < 1:
        # cek durasi
        classes = "invalid (durasi 0 detik)"
        status = 200
    elif audio_info.channels != 1:
        # cek channels
        classes = "channels tidak 1"
    elif audio_info.sample_rate != 48_000:
        # cek sample rate
        classes = "sample rate tidak 48.000 Hz"

    if classes == "":
        # jika classes kosong atau tidak melakukan update
        # audio valid
        return True

    # audio tidak valid
    # update data menggunakan PUT API
    # update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}&deviceCode={device_code}&id={result_id}&msisdn={msisdn}&status={status}&desc={classes}"
    # status_code = requests.put(update_url).status_code

    # log file
    print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}")
    # print(f"{datetime.now()}\t PUT Status: {status_code}")

    return False

def main():
    """
        Fungsi main untuk melakukan GET dan PUT dengan hasil aduio apakah terdapat ringing atau tidak dan termasuk dalam kelas valid atau invalid
    """

    try:
        # GET API URL
        # file_path = "audio/" + random.choice([file for file in os.listdir("audio") if file.endswith('wav')])
        file_path = "test/valid(2).wav"
        # get_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}"
        # result_get = requests.get(get_url)

        # if result_get.status_code >= 300:
        #     # jika status code GET tidak 200
        #     # log file
        #     # print(f"{datetime.now()}\t GET Status: {result_get.status_code}")

        #     return

        # result_json = result_get.json()
        # audio_url, msisdn, result_id, device_code = result_json.get('path'), result_json.get('msisdn'), result_json.get('id'), result_json.get('deviceCode')

        # log file
        # print(f"{datetime.now()}\t GET Status: {result_get.status_code}, id: {result_id}")

        # filename untuk file audio
        # filename = msisdn + "_" + str(time.time()) + '.wav'
        # download file dari URL yang didapat dari API
        # file_path = file_downloader(audio_url, filename)
        file_path = samplerate_conv(file_path)

        # cek validasi audio
        # valid = validate_audio(file_path, filename, result_id, msisdn, device_code)
        # if not valid:
        #     return
    except Exception as e:
        # audio gagal diproses
        # log file
        print(f"{datetime.now()}\t[Error]")
        print(e)
        # print(get_url)
        # print(audio_url)
        return

    try:
        # coba proses audio
        strt_process = time.perf_counter()
        # cek file audio ada ringing atau tidak
        provider = random.choice(['ISAT', 'AXIS'])
        classes, status = ringing_recognition(file_path, provider)

        ttl_process = str(round(time.perf_counter() - strt_process, 2)) + "s"

        # log file
        # print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}, Time Process: {ttl_process}")

        # update data menggunakan PUT API
        # update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}&deviceCode={device_code}&id={result_id}&msisdn={msisdn}&status={status}&desc={classes}"
        # status_code = requests.put(update_url).status_code
        print(file_path, status, classes, provider)

        # log file
        # print(f"{datetime.now()}\t PUT Status: {status_code}")
        os.remove(file_path)
    except Exception as e:
        # audio gagal diproses
        # log file
        print(f"{datetime.now()}\t[Error]")
        print(e)
        # print(f"{result_id}, {audio_url}, {msisdn}")
        # print(audio_metadata.load(f"audio/{filename}"))

# reset = True
# AUDIO_PATH = "audiob"
while True:
    main()
#     if reset:
#         start = time.perf_counter()
#         reset = False

    # main()
#     time.sleep(COOLDOWN)

#     if (time.perf_counter() - start) >= 10:
#         shutil.rmtree(AUDIO_PATH)
#         os.makedirs(AUDIO_PATH, exist_ok=True)
#         reset = True
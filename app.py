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

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
DEVICE_CODE = config("DEVICE_CODE")
AUDIO_PATH = "audio"
RESET = True

def validate_audio(file_path, filename, r_id, msisdn):
    """
        docstring
    """

    classes = ""
    status = 3
    update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?deviceCode={DEVICE_CODE}&id={r_id}&msisdn={msisdn}"
    audio_info = WAVE(file_path).info

    if audio_info.length < 1:
        classes = "durasi 0 detik"
    elif audio_info.channels != 1:
        classes = "channels tidak 1"
    elif audio_info.sample_rate != 48_000:
        classes = "sample rate tidak 48.000 Hz"

    if classes == "":
        return True

    update_url = update_url + f"&status={status}&desc={classes}"
    status_code = requests.put(update_url).status_code
    print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}")
    print(f"{datetime.now()}\t PUT Status: {status_code}")

    return False

def main():
    """
        docstring
    """

    url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?deviceCode={DEVICE_CODE}"
    r_get = requests.get(url)
    if r_get.status_code >= 300:
        print(f"{datetime.now()}\t GET Status: {r_get.status_code}")
        return

    r_json = r_get.json()
    audio_url, msisdn, r_id = r_json.get('path'), r_json.get('msisdn'), r_json.get('id')

    print(f"{datetime.now()}\t GET Status: {r_get.status_code}, id: {r_id}")

    filename = msisdn + "_" + str(time.time()) + '.wav'
    file_path = file_downloader(audio_url, filename)

    valid = validate_audio(file_path, filename, r_id, msisdn)
    if not valid:
        return

    try:
        strt_process = time.perf_counter()
        classes, status = ringing_recognition(file_path)
        ttl_process = str(round(time.perf_counter() - strt_process, 2)) + "s"

        print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}, Time Process: {ttl_process}")

        update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?deviceCode={DEVICE_CODE}&id={r_id}&msisdn={msisdn}&status={status}&desc={classes}"
        r_update = requests.put(update_url)

        print(f"{datetime.now()}\t PUT Status: {r_update.status_code}")
    except NameError:
        print(datetime.now())
        print(f"{r_id}, {audio_url}, {msisdn} [Error]")
        print(audio_metadata.load(f"audio/{filename}"))

while True:
    if RESET:
        start = time.perf_counter()
        RESET = False

    main()
    time.sleep(COOLDOWN)

    if (time.perf_counter() - start) >= 3600:
        shutil.rmtree(AUDIO_PATH)
        os.makedirs(AUDIO_PATH, exist_ok=True)
        RESET = True

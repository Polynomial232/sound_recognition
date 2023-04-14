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

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
DEVICE_CODE = config("DEVICE_CODE")
REMOVE_AUDIO = config("REMOVE_AUDIO")

def main():
    """
        docstring
    """

    url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?deviceCode={DEVICE_CODE}"
    r_get = requests.get(url)
    if r_get.status_code >= 300:
        return

    r_json = r_get.json() if r_get.status_code < 300 else "Fail"

    audio_url = r_json.get('path') if r_get.status_code < 300 else "http://52.197.203.216/voice/callrecord.wav"
    msisdn = r_json.get('msisdn') if r_get.status_code < 300 else "test"
    r_id = r_json.get('id') if r_get.status_code < 300 else "id"

    print(f"{datetime.now()}\t GET Status: {r_get.status_code}, id: {r_id}")

    filename = msisdn + "_" + str(time.time()) + '.wav'

    strt_process = time.perf_counter()
    file_path = file_downloader(audio_url, filename)
    classes, status = ringing_recognition(file_path)
    ttl_process = round(time.perf_counter() - strt_process, 2)
    ttl_process = f"{ttl_process}s"

    print(f"{datetime.now()}\t Status: {status}, Deskripsi: {classes}, Time Process: {ttl_process}")

    update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?deviceCode={DEVICE_CODE}&id={r_id}&msisdn={msisdn}&status={status}&desc={classes}"
    r_update = requests.put(update_url)

    print(f"{datetime.now()}\t PUT Status: {r_update.status_code}")
    _ = r_update.json() if r_update.status_code < 300 else "Fail"
    if REMOVE_AUDIO.lower() == "true":
        os.rm(f"audio/{filename}")

while True:
    main()
    time.sleep(COOLDOWN)

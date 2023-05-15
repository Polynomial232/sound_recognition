"""
    docstring
"""
# pylint: disable=line-too-long, unused-import

import time
import os
import json
from datetime import datetime
import shutil
import requests
import audio_metadata
from decouple import config
from mutagen.wave import WAVE

from ringing_detection import ringing_recognition
from functions.file_downloader import audio_downloader
from functions.samplerate_conv import samplerate_conv

COOLDOWN = int(config("COOLDOWN"))
IP_API = config("IP_API")
PORT_API = config("PORT_API")
PC_CODE = config("PC_CODE")
TIME_DELETE = config("TIME_DELETE")

AUDIO_PATH = "audio"
RESET = True

def validate_audio(file_path, filename, result_id, msisdn, device_code):
    """
        Mengecek apakah audio sudah sesuai standar atau belum
        durasi audio tidak boleh 0
        channels audio 1
        sample rate 48_000 Hz
    """

    with open('json/audio_info_status.json', 'r', encoding='utf-8') as file:
        audio_info_status = json.loads(file.read())

    classes = None

    audio_info = WAVE(file_path).info

    if audio_info.length < 1:
        classes, status = audio_info_status.get("detik").values()
    elif audio_info.channels != 1:
        classes, status = audio_info_status.get("channels").values()
    elif audio_info.sample_rate != 48_000:
        classes, status = audio_info_status.get("sample_rate").values()

    if classes is None:
        return True

    update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}&deviceCode={device_code}&id={result_id}&msisdn={msisdn}&status={status}&desc={classes}"
    status_code = requests.put(update_url).status_code

    print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}")
    print(f"{datetime.now()}\t PUT Status: {status_code}")

    return False

def main():
    """
        Fungsi main untuk melakukan GET dan PUT dengan hasil aduio apakah terdapat ringing atau tidak dan termasuk dalam kelas valid atau invalid
    """
    # pylint: disable=too-many-locals, broad-except, invalid-name

    try:
        get_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}"
        result_get = requests.get(get_url)

        if result_get.status_code >= 300:
            # print(f"{datetime.now()}\t GET Status: {result_get.status_code}")
            return

        result_json = result_get.json()
        audio_url, msisdn, result_id, device_code, provider = result_json.get('path'), result_json.get('msisdn'), result_json.get('id'), result_json.get('deviceCode'), result_json.get('prefix')

        print(f"{datetime.now()}\t GET Status: {result_get.status_code}, id: {result_id}")

        filename = msisdn + "_" + str(time.time()) + '.wav'
        file_path = audio_downloader(audio_url, filename)
        file_path = samplerate_conv(file_path)

        valid = validate_audio(file_path, filename, result_id, msisdn, device_code)

        delete_url = audio_url.replace('download', 'delete')
        result_delete = requests.get(delete_url)
        print(result_delete)
        if not valid:
            return
    except Exception as e:
        print(f"{datetime.now()}\t[Error]")
        print(e)
        if result_get.status_code <= 300:
            print(audio_url)
        return

    try:
        strt_process = time.perf_counter()
        classes, status = ringing_recognition(file_path, provider)

        ttl_process = str(round(time.perf_counter() - strt_process, 2)) + "s"

        print(f"{datetime.now()}\t {filename}, Status: {status}, Deskripsi: {classes}, Time Process: {ttl_process}")

        update_url = f"http://{IP_API}:{PORT_API}/kamikaze/voiceCheck?pcCode={PC_CODE}&deviceCode={device_code}&id={result_id}&msisdn={msisdn}&status={status}&desc={classes}"
        status_code = requests.put(update_url).status_code

        print(f"{datetime.now()}\t PUT Status: {status_code}")

        os.remove(file_path)

        with open('logs/_logs.csv', 'a', encoding='utf-8') as logs_file:
            logs_file.write(f'{device_code},{msisdn},{provider},{status},{classes},{ttl_process}\n')

    except Exception as e:
        print(f"{datetime.now()}\t[Error]")
        print(e)
        print(f"{result_id}, {audio_url}, {msisdn}")
        print(audio_metadata.load(f"audio/{filename}"))


while True:
    if RESET:
        start = time.perf_counter()
        RESET = False

    main()
    time.sleep(COOLDOWN)

    if (time.perf_counter() - start) >= int(TIME_DELETE):
        shutil.rmtree(AUDIO_PATH)
        os.makedirs(AUDIO_PATH, exist_ok=True)
        RESET = True

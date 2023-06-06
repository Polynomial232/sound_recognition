"""
    docstring
"""
# pylint: disable=line-too-long, unused-import

import time
import os
from datetime import datetime
import shutil
import audio_metadata
from decouple import config

from ringing_detection import ringing_recognition
from functions.file_downloader import audio_downloader
from functions.samplerate_conv import samplerate_conv
from functions.validate_audio import validate_audio
from functions.api_action import do_put, do_get

COOLDOWN = int(config("COOLDOWN"))
TIME_DELETE = config("TIME_DELETE")

AUDIO_PATH = "audio"
RESET = True

def main():
    """
        Fungsi main untuk melakukan GET dan PUT dengan hasil aduio apakah terdapat ringing atau tidak dan termasuk dalam kelas valid atau invalid
    """
    # pylint: disable=too-many-locals, broad-except, invalid-name

    try:
        result_get = do_get()

        if result_get.status_code >= 300:
            print(f"{datetime.now()}\t GET Status: {result_get.status_code}")
            return result_get.status_code

        result_json = result_get.json()
        audio_url, msisdn, result_id, device_code, provider = result_json.get('path'), result_json.get('msisdn'), result_json.get('id'), result_json.get('deviceCode'), result_json.get('prefix')

        print(f"{datetime.now()}\t GET Status: {result_get.status_code}, id: {result_id}")

        filename = audio_url.split('download?name=')[1]
        file_path_raw = audio_downloader(audio_url, filename)
        file_path, error = samplerate_conv(file_path_raw)
        if error:
            do_put(
                filename=filename,
                device_code=device_code,
                result_id=result_id,
                msisdn=msisdn,
                status=3,
                classes="unknown (masalah audio)",
            )

        valid = validate_audio(file_path, filename, result_id, msisdn, device_code)

        if not valid:
            return 200
    except Exception as e:
        print(f"{datetime.now()}\t[Error]")
        print(e)
        return 400

    try:
        strt_process = time.perf_counter()
        classes, status, text = ringing_recognition(file_path, provider)
        ttl_process = str(round(time.perf_counter() - strt_process, 2)) + "s"

        do_put(
            filename=filename,
            device_code=device_code,
            result_id=result_id,
            msisdn=msisdn,
            status=status,
            classes=classes,
            ttl_process=ttl_process,
            text=text
        )

        os.remove(file_path)

        with open('logs/_logs.csv', 'a', encoding='utf-8') as logs_file:
            logs_file.write(f'{device_code},{msisdn},{provider},{status},{classes},{ttl_process}\n')

    except Exception as e:
        print(f"{datetime.now()}\t[Error]")
        print(e)
        print(f"{result_id}, {audio_url}, {msisdn}")
        print(audio_metadata.load(file_path_raw))

        return 200

    return result_get.status_code

while True:
    if RESET:
        start = time.perf_counter()
        RESET = False

    status_code = main()
    cooldown = COOLDOWN if status_code != 400 else 5
    time.sleep(cooldown)

    if (time.perf_counter() - start) >= int(TIME_DELETE):
        shutil.rmtree(AUDIO_PATH)
        os.makedirs(AUDIO_PATH, exist_ok=True)
        RESET = True

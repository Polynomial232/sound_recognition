
import json
from mutagen.wave import WAVE
from .api_action import do_put

with open('json/audio_info_status.json', 'r', encoding='utf-8') as file:
    AUDIO_INFO_STATUS = json.loads(file.read())

def validate_audio(file_path, filename, result_id, msisdn, device_code):
    """
        Mengecek apakah audio sudah sesuai standar atau belum
        durasi audio tidak boleh 0
        channels audio 1
        sample rate 48_000 Hz
    """

    classes = None

    audio_info = WAVE(file_path).info

    if audio_info.length < 1:
        classes, status = AUDIO_INFO_STATUS.get("detik").values()
    elif audio_info.channels != 1:
        classes, status = AUDIO_INFO_STATUS.get("channels").values()
    elif audio_info.sample_rate != 48_000:
        classes, status = AUDIO_INFO_STATUS.get("sample_rate").values()

    if classes is None:
        return True

    do_put(
        filename=filename,
        device_code=device_code,
        result_id=result_id,
        msisdn=msisdn,
        status=status,
        classes=classes,
    )

    return False

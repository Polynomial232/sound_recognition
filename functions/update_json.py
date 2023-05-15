from functions.file_downloader import file_downloader

def update_json():
    file_downloader('https://raw.githubusercontent.com/Polynomial232/sound_recognition/dev/json/audio_info_status.json', 'json/audio_info_status.json')
    file_downloader('https://raw.githubusercontent.com/Polynomial232/sound_recognition/dev/json/decision.json', 'json/decision.json')

"""
    kumpulan beberapa fungsi
"""

import json
from datetime import datetime
from difflib import SequenceMatcher

CASUAL_FILE = 'model/casual_intents.json'
ERROR = 0.8

with open(CASUAL_FILE, 'r', encoding='utf-8') as f:
    casual_intents = json.loads(f.read())

def re_write_json(filename, content):
    """
        menulis kembali file.json
    """

    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(content,
                  json_file,
                  indent=4,
                  separators=(',',': '))

def current_date():
    """
        mendapatkan waktu saat ini
    """

    return datetime.timestamp(datetime.now())

def similar(v_1, v_2):
    """
        mengecek apakah text1 mirip dengan text2
    """

    return SequenceMatcher(None, v_1.lower(), v_2.lower()).ratio()

def predict_casual(text):
    """
        prediksi jawaban casual seperti ya, tidak ulangi
    """

    prob_arr = []
    id_arr = []

    for _, intent in enumerate(casual_intents.get('intents')):
        for pattern in intent.get('patterns'):
            id_arr.append(intent.get('id'))
            prob_arr.append(similar(text, pattern))

    max_prob = max(prob_arr)

    if max_prob <= ERROR:
        return []

    get_id = id_arr[prob_arr.index(max(prob_arr))]

    for intent in casual_intents.get('intents'):
        if get_id == intent.get('id'):
            break

    return intent

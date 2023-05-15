"""
    docstring
"""

import os
import requests

def audio_downloader(url, filename):
    """
        docstring
    """

    file_path = os.path.join('audio', filename)

    r_get = requests.get(url, allow_redirects=True, timeout=10)

    with open(file_path, 'wb') as file:
        file.write(r_get.content)

    return file_path

def model_downloader(url, filename):
    """
        docstring
    """

    file_path = os.path.join('text_classification', 'model', filename)

    r_get = requests.get(url, allow_redirects=True, timeout=10)

    with open(file_path, 'wb') as file:
        file.write(r_get.content)

    return file_path


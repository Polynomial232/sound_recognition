"""
    docstring
"""

from zipfile import ZipFile

def unzip(path):
    """
        docstring
    """

    with ZipFile(path, 'r') as z_object:
        z_object.extractall('audio')

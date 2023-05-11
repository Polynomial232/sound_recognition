"""
    docstring
"""

from zipfile import ZipFile

def unzip(path):
    """
        docstring
    """

    with ZipFile(path, 'r') as zObject:
        zObject.extractall('audio')

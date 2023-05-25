"""
    docstring
"""

from text_classification.classes.Train import Train
import time

train = Train(400)
train.start()

with open('text_classification/model/updated_at.txt', 'w', encoding='utf-8') as file:
    file.write(str(time.time()))

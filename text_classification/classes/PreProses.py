# pylint: disable=invalid-name
"""
    kelas Pre Prosesing untuk data Train
"""

import json
import numpy as np
import nltk
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#nltk.download('punkt')

factory = StemmerFactory()
stemmer = factory.create_stemmer()


class PreProses():
    """
        kelas Pre Prosessing
    """

    def __init__(self):

        with open(f'text_classification/model/intents.json',
                  'r', encoding='utf-8') as file:
            intents = json.loads(file.read())
        self.intents = intents
        self.ignore_words = list("\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~")

    def get_intents(self):
        """
            mendapatkan intents dari file.json
        """

        return self.intents

    def tokenizing(self, sentence):
        """
            pemisahan kata dalam suatu kalimat
        """

        return nltk.word_tokenize(sentence)

    def stemming(self, word):
        """
            mengubah kata menjadi kata dasar
        """

        return stemmer.stem(word.lower())

    def bag_of_words(self, tokenized_sentence, words):
        """
            menyumpan kata kedalam array
        """

        sentence_words = [self.stemming(word) for word in tokenized_sentence]
        bag = np.zeros(len(words), dtype=np.float32)

        for idx, word in enumerate(words):
            if word in sentence_words:
                bag[idx] = 1

        return bag

    def get_raw_data(self):
        """
            mendapatkan semua data tag dan text
        """

        tags = []
        all_words = []

        for intent in self.intents.get('intents'):
            tag = intent.get('tag')
            tags.append(tag)
            for pattern in intent.get('patterns'):
                if pattern is None:
                    continue
                word = self.tokenizing(pattern)
                all_words.extend(word)

        all_words = [self.stemming(
            word) for word in all_words if word not in self.ignore_words]
        all_words = sorted(set(all_words))
        tags = sorted(set(tags))

        return tags, all_words

    def train_data(self):
        """
            memisahkan data menjadi data train dan data kelas
        """

        all_words = []
        tags = []
        train_test = []

        for intent in self.intents.get('intents'):
            tag = intent.get('tag')
            tags.append(tag)
            for pattern in intent.get('patterns'):
                if pattern is None:
                    continue
                word = self.tokenizing(pattern)
                all_words.extend(word)
                train_test.append((word, tag))

        all_words = [self.stemming(
            word) for word in all_words if word not in self.ignore_words]
        all_words = sorted(set(all_words))
        tags = sorted(set(tags))

        x_train = []
        y_train = []

        for (pattern_sentence, tag) in train_test:
            bag = self.bag_of_words(pattern_sentence, all_words)
            x_train.append(bag)

            label = tags.index(tag)
            y_train.append(label)

        return x_train, y_train

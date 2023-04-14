# pylint: disable=invalid-name
"""
    kelas untuk melakukan Pelatihan Deep Learning
"""

import time
import json
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

from text_classification.classes.PreProses import PreProses
from text_classification.classes.ChatDataset import ChatDataset
from text_classification.classes.NeuralNet import NeuralNet


class Train():
    """
        kelas Train
    """

    def __init__(self, epochs=1000):
        self.epochs = epochs
        self.data = None

    def start(self):
        """
            melakukan pelatihan Deep Learning Chatbot
        """

        pre_proses = PreProses()

        tags, all_words = pre_proses.get_raw_data()
        x_train, y_train = pre_proses.train_data()

        chat_dataset = ChatDataset(x_train, y_train)

        batch_size = 8
        train_loader = DataLoader(dataset=chat_dataset,
                                  batch_size=batch_size,
                                  shuffle=True,
                                  num_workers=0)
        hidden_size = 8
        output_size = len(tags)
        input_size = len(x_train[0])

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        model = NeuralNet(input_size, hidden_size, output_size).to(device)

        learning_rate = 0.001
        num_epochs = self.epochs
        history = []

        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

        for epoch in range(num_epochs):
            for (words, labels) in train_loader:
                words = words.to(device)
                labels = labels.to(device)

                output = model(words)
                loss = criterion(output, labels)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            history.append(f'{loss.item():.4f}')
            if (epoch+1) % 100 == 0:
                print(f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}')

        self.data = {
            "model_state": model.state_dict(),
            "input_size": input_size,
            "output_size": output_size,
            "hidden_size": hidden_size,
            "all_words": all_words,
            "tags": tags,
            "history": history,
            "updated_at": time.time()
        }

        file = f'text_classification/model/data.pth'
        torch.save(self.data, file)

        return self.data

    def currect_train(self):
        """
            mendapatkan hasil Pelatihan terakhir seperti akurasi dan tingkat kesalahan
        """

        data = {
            "last_loss": self.data.get('history')[:1][0],
            "min_loss": min(self.data.get('history')),
            "image_history": f'text_classification/model/histroy_train.jpg',
            "updated_at": self.data.get('updated_at')
        }

        with open(f'text_classification/model/current.json',
                  'w', encoding='utf-8') as file:
            json.dump(data, file,
                      indent=4,
                      separators=(',', ': '))

        return data

    def plot_history(self):
        """
            docstring
        """

        loss = list(map(float, self.data.get('history')))

        _, (ax1) = plt.subplots(figsize=(10, 4))
        ax1.plot(loss, label='loss')
        ax1.legend(loc='lower right')
        plt.savefig(
            f'text_classification/model/histroy_train.jpg')

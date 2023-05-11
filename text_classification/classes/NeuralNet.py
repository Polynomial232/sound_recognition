# pylint: disable=invalid-name
"""
    kelas pembuatan jaringan saraf untuk Deep Learning
"""


from torch import nn

class NeuralNet(nn.Module):
    """
        kelas NeuralNet
    """

    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        # super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        """
            fungsi pembuatan jaringan saraf
        """
        # pylint: disable=invalid-name

        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)

        return out

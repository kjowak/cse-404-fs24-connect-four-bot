import torch.nn as nn

class Connect4Bot(nn.Module):
    def __init__(self):
        super(Connect4Bot, self).__init__()
        self.flatten = nn.Flatten()

        self.convolutional_stack = nn.Sequential(
            nn.Conv2d(1, 42, 4, padding=1),
            nn.Tanh(),
            nn.MaxPool2d(2, stride=2),
        )

        self.linear = nn.Sequential(
            nn.Linear(6, 1),
            nn.Sigmoid()
        )


    def forward(self, x):
        x = self.convolutional_stack(x)
        x = self.flatten(x)
        logits = self.linear(x)
        return logits
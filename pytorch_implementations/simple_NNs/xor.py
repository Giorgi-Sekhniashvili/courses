import torch


class XOR_model(torch.nn.Module):
    def __init__(self):
        super(XOR_model, self).__init__()
        self.fc_1 = torch.nn.Linear(in_features=2, out_features=2)
        self.fc_2 = torch.nn.Linear(in_features=2, out_features=1)

    def forward(self, x):
        out = torch.sigmoid(self.fc_1(x))
        out = torch.sigmoid(self.fc_2(out))
        return out


if __name__ == '__main__':
    data = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float32, requires_grad=False)
    targets = torch.tensor([0, 1, 1, 0], dtype=torch.float32, requires_grad=False).view((4, 1))

    model = XOR_model()
    optimizer = torch.optim.SGD(params=model.parameters(), lr=0.1)
    loss_fn = torch.nn.BCELoss()

    epochs = 10000
    model.train()

    for i in range(epochs):
        outputs = model(data)

        loss = loss_fn(outputs, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    model.eval()
    out = model(data)


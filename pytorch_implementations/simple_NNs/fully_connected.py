import torch
import torch.nn.functional as F
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class SimpleFC(torch.nn.Module):
    def __init__(self, in_features, num_classes):
        super(SimpleFC, self).__init__()
        self.fc_1 = torch.nn.Linear(in_features=in_features, out_features=16)
        self.fc_2 = torch.nn.Linear(in_features=16, out_features=16)
        self.fc_3 = torch.nn.Linear(in_features=16, out_features=16)
        self.fc_4 = torch.nn.Linear(in_features=16, out_features=16)
        self.fc_5 = torch.nn.Linear(in_features=16, out_features=num_classes)
        self.batch_norm = torch.nn.BatchNorm1d(16)
        self.dropout = torch.nn.Dropout(p=0.3)

    def forward(self, inp_tensor):
        output_tensor = F.relu(self.fc_1(inp_tensor))
        output_tensor = self.dropout(output_tensor)
        output_tensor = self.batch_norm(output_tensor)

        output_tensor = F.relu(self.fc_2(output_tensor))
        output_tensor = self.dropout(output_tensor)
        output_tensor = self.batch_norm(output_tensor)

        output_tensor = F.relu(self.fc_3(output_tensor))
        output_tensor = self.dropout(output_tensor)
        output_tensor = self.batch_norm(output_tensor)

        output_tensor = F.relu(self.fc_4(output_tensor))
        output_tensor = self.dropout(output_tensor)
        output_tensor = self.batch_norm(output_tensor)

        output_tensor = self.fc_5(output_tensor)
        return output_tensor


if __name__ == '__main__':
    iris = load_iris()

    data = torch.from_numpy(iris['data']).float()
    labels = torch.from_numpy(iris['target']).long()

    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.3)

    print('train test sizes', train_data.shape, test_data.shape, train_labels.shape, test_labels.shape)

    my_model = SimpleFC(4, 3)

    optimizer = torch.optim.Adam(my_model.parameters(), lr=0.01, weight_decay=0.1)
    loss_fn = torch.nn.CrossEntropyLoss()

    epochs = 50

    history = {
        'loss': [],
        'correct': 0,
        'total': 0
    }

    for i in range(epochs):
        my_model.train()

        outputs = my_model(train_data)

        optimizer.zero_grad()
        loss = loss_fn(outputs, train_labels)
        loss.backward()
        optimizer.step()

        history['loss'].append(loss.item())
        _, output_classes = torch.max(outputs, dim=1)
        history['total'] += train_labels.shape[0]
        history['correct'] += int((output_classes == train_labels).sum())

        if i % 100 == 0:
            print(f'Epoch: {i}')

    print(f"\ntrain accuracy = {history['correct'] / history['total']}")

    my_model.eval()
    test_outputs = my_model(test_data)
    _, output_classes = torch.max(test_outputs, dim=1)

    acc = accuracy_score(test_labels.detach().numpy(), output_classes.detach().numpy())

    print(f"\ntest accuracy = {acc}")

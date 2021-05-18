import torch
from torch.utils.data.dataloader import DataLoader

device = torch.device('gpu' if torch.cuda.is_available() else 'cpu')


def train(model, loss_fn, optimizer,
          train_data_loader: DataLoader, epochs: int = 100, verbose: bool = False) -> dict:
    """train your model with this"""

    model.to(device).train()

    history = {
        'loss': [],
        'correct': 0,
        'total': 0
    }
    for epoch in range(epochs):
        print(f'Epoch: {epoch}')
        for i, (data, labels) in enumerate(train_data_loader):
            data, labels = data.to(device), labels.to(device)
            outputs = model(data)

            loss = loss_fn(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            history['loss'].append(loss.item())
            _, output_classes = torch.max(outputs, dim=1)
            history['total'] += labels.shape[0]
            history['correct'] += int((output_classes == labels).sum())

            if i % 100 == 0 and verbose:
                print(f'Epoch: {epoch}, Iteration: {i}, Loss: {loss}')

    model.eval()
    return history


def test(model, loss_fn, test_data_loader: DataLoader):

    model.to(device).eval()

    metadata = {
        'test_loss': [],
        'correct': 0,
        'total': 0
    }

    for i, (data, labels) in enumerate(test_data_loader):
        data, labels = data.to(device), labels.to(device)

        outputs = model(data)

        loss = loss_fn(outputs, labels)
        metadata['test_loss'].append(loss)

        _, output_classes = torch.max(outputs, dim=1)
        metadata['total'] += labels.shape[0]
        metadata['correct'] += int((output_classes == labels).sum())

    return metadata

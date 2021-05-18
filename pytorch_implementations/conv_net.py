import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from simple_NNs import ConvNet
from utils import train, test

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

print(f'device: {device}')
dataset_path = r'C:\Users\gsekhniashvili\Desktop\BOG\Datasets\MNIST'

mnist_train = datasets.MNIST(dataset_path,
                             train=True,
                             download=False,
                             transform=transforms.ToTensor())

mnist_test = datasets.MNIST(dataset_path,
                            train=False,
                            download=False,
                            transform=transforms.ToTensor())

print('size of mnist training data = ', len(mnist_train))
print('size of mnist testing data = ', len(mnist_test))

train_data_loader = DataLoader(dataset=mnist_train, batch_size=128, shuffle=True)
test_data_loader = DataLoader(dataset=mnist_test, batch_size=128, shuffle=True)

conv_net = ConvNet(in_channels=1)

loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(params=conv_net.parameters(), lr=0.01)

train_hist = train(model=conv_net, loss_fn=loss_fn, optimizer=optimizer, train_data_loader=train_data_loader, epochs=4)

print(f"\ntrain accuracy = {train_hist['correct'] / train_hist['total']}")

test_hist = test(model=conv_net, loss_fn=loss_fn, test_data_loader=test_data_loader)
print(f"\ntest accuracy = {test_hist['correct'] / test_hist['total']}")

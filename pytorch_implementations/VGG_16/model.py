import torch

vgg_16 = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M']


class VGG(torch.nn.Module):
    def __init__(self, in_channels, num_classes, architecture: list = vgg_16):
        super(VGG, self).__init__()
        self.in_channels = in_channels
        self.num_classes = num_classes
        self.architecture = architecture
        self.conv_layers = self.create_conv_layers(architecture=self.architecture)

        self.fc = torch.nn.Sequential(
            torch.nn.Flatten(),
            torch.nn.Linear(512 * 7 * 7, 4096),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(4096, 4096),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.5),
            torch.nn.Linear(4096, self.num_classes)
        )

    def forward(self, inp: torch.Tensor):
        x = self.conv_layers(inp)
        out = self.fc(x)

        return out

    def create_conv_layers(self, architecture):
        layers = []
        in_channels = self.in_channels
        for x in architecture:
            if type(x) == int:
                out_channels = x

                layers += [
                    torch.nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, padding=1),
                    torch.nn.BatchNorm2d(num_features=out_channels),
                    torch.nn.ReLU()]
                in_channels = x
            elif x == 'M':
                layers += [torch.nn.MaxPool2d(kernel_size=2, stride=2)]

        return torch.nn.Sequential(*layers)


if __name__ == '__main__':
    x = torch.randn(4, 3, 224, 224)
    model = VGG(in_channels=3, num_classes=10)
    print(model)
    out = model(x)


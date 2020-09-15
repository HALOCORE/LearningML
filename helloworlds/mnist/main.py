import torch
from torchvision import datasets

def main():
    dataset1 = datasets.MNIST('./data', train=True, download=True, transform=None)
    dataset2 = datasets.MNIST('./data', train=False, download=True, transform=None)
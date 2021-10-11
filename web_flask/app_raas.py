#!/usr/bin/python3

from models import storage
from models.receiver import Receiver

# print(storage.all('Receiver').values())
for key, values in storage.all('Receiver').items():
    print(key, values.to_dict())

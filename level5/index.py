#!/usr/bin/env python
import requests
import pickle

pickle_text = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").text
data = pickle.loads(str.encode(pickle_text))

for line in data:
    print("".join([char * num  for char, num in line]))

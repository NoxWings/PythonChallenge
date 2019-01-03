#!/usr/bin/env python
import requests
import re

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}"
next_param = input()

while next_param:
    response = requests.get(base_url.format(next_param))
    match = re.search(r"and the next nothing is (\d+)", response.text)
    if match:
        next_param = match.group(1)
        print("param: {}".format(next_param))
    else:
        next_param = None
        print(response.text)

import requests
import os.path


def download_file(url, filepath, force_download=False):
    if (not os.path.exists(filepath) or force_download):
        _download_file(url, filepath)
    return filepath


def _download_file(url, filepath):
    response = requests.get(url, stream=True)
    with open(filepath, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "oxygen.png")
download_file("http://www.pythonchallenge.com/pc/def/oxygen.png", filepath)

# ------------------------------------------------------------------------------

from PIL import Image
import re

def pixel_value(pix, x, y):
    r, g, b, _ = pix[x, y]
    if (r == g) and (g == b):
        return chr(r)

im = Image.open(filepath)
pix = im.load()

width, height = im.size

hint = ""
for x in [i for i in range(width) if (i % 7) == 0]:
    c = pixel_value(pix, x, height // 2)
    if (c):
        hint += c
print(hint)

secret_part = re.search(r"\[.*?\]", hint).group(0)
secret = "".join(chr(int(n)) for n in secret_part[1:-1].split(", "))
print("{} = {}".format(secret_part, secret))

import os.path
import requests
from zipfile import ZipFile
import re

def download_file(url, file_path):
    response = requests.get(url, stream=True)
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

def download_file_cached(url, filename):
    directory = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(directory, filename)
    if (not os.path.exists(filepath)):
        download_file(url, filepath)
    return filepath

def follow_numbers(zip_file, next_filename):
    comments = ""
    while next_filename:
        number_filename = "{}.txt".format(next_filename)
        with myzip.open(number_filename) as myfile:
            text = myfile.read().decode()
            match = re.search(r"\b\d+\b", text)
            next_filename = match.group(0) if match else None
            if (not next_filename):
                print(text)
            comments += myzip.getinfo(number_filename).comment.decode()
    print(comments)


url = "http://www.pythonchallenge.com/pc/def/channel.zip"
filename = "level6.zip"
filepath = download_file_cached(url, filename)

with ZipFile(filepath) as myzip:
    follow_numbers(myzip, "readme")

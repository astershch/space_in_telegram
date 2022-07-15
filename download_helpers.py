import os

import requests

from pathlib import Path
from urllib.parse import urlparse


def get_file_extension(url):

    parsed_url = urlparse(url)
    extension = os.path.splitext(parsed_url.path)[-1]

    return extension


def download_image(url, path, params=None):

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def create_directory(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)

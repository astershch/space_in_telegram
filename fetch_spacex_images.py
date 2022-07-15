import argparse
import os

import requests

from pathlib import Path

from dotenv import load_dotenv

from download_helpers import download_image, create_directory


def fetch_spacex_images(url, directory, params):

    response = requests.get(url, params)
    response.raise_for_status()
    useful_response = response.json()['links']['flickr']['original']

    for index, image_url in enumerate(useful_response):
        download_image(
            image_url,
            Path(directory, f'spacex_{index}.jpg'),
        )


def main():

    load_dotenv()

    spacex_url = os.environ['SPACEX_URL']
    images_directory = os.environ['IMAGES_DIRECTORY']

    create_directory(images_directory)

    request_params = None

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'flight_id',
        help='use to get images of specific flight id or get latest if None',
        nargs='?',
    )
    args = parser.parse_args()

    if args.flight_id is None:
        spacex_url += '/latest'
    else:
        spacex_url += f'/{args.flight_id}'

    fetch_spacex_images(spacex_url, images_directory, request_params)


if __name__ == '__main__':
    main()

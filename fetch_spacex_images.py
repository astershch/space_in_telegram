import argparse
import os

import requests

from pathlib import Path

from dotenv import load_dotenv

from download_helpers import download_image


def fetch_spacex_images(flight_id, directory):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{flight_id}'

    response = requests.get(spacex_url)
    response.raise_for_status()
    useful_response = response.json()['links']['flickr']['original']

    for index, image_url in enumerate(useful_response):
        download_image(
            image_url,
            Path(directory, f'spacex_{index}.jpg'),
        )


def main():

    load_dotenv()

    images_directory = os.environ['IMAGES_DIRECTORY']

    Path(images_directory).mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'flight_id',
        help='use to get images of specific flight id or get latest if None',
        nargs='?',
        default='latest',
    )
    args = parser.parse_args()

    fetch_spacex_images(args.flight_id, images_directory)


if __name__ == '__main__':
    main()

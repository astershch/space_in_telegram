import os

import requests

from pathlib import Path

from dotenv import load_dotenv

from download_helpers import (
    create_directory,
    download_image,
    get_file_extension,
)


def fetch_nasa_apod_images(url, params, directory):

    response = requests.get(url, params=params)
    response.raise_for_status()

    for index, media in enumerate(response.json()):
        if media.get('media_type') == 'image':
            image_url = media['hdurl']
            image_extension = get_file_extension(image_url)
            download_image(
                image_url,
                Path(directory, f'nasa_apod_{index}{image_extension}'),
            )


def main():

    load_dotenv()

    nasa_apod_url = os.environ['NASA_APOD_URL']
    nasa_api_token = os.environ['NASA_API_TOKEN']
    images_directory = os.environ['IMAGES_DIRECTORY']

    create_directory(images_directory)

    nasa_request_params = {
        'api_key': nasa_api_token,
        'count': 30,
    }

    fetch_nasa_apod_images(
        nasa_apod_url,
        nasa_request_params,
        images_directory
    )


if __name__ == '__main__':
    main()

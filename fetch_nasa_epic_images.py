import datetime
import os

import requests

from pathlib import Path

from dotenv import load_dotenv

from download_helpers import create_directory, download_image


def fetch_nasa_epic_images(url, params, directory):

    response = requests.get(url, params=params)
    response.raise_for_status()

    for index, image in enumerate(response.json()):
        image_name = image['image']
        image_date = (
            datetime
            .datetime
            .fromisoformat(image['date'])
            .strftime('%Y/%m/%d')
        )

        image_url = (
            f'https://api.nasa.gov/EPIC/archive/natural'
            f'/{image_date}/png/{image_name}.png'
        )

        download_image(
            image_url,
            Path(directory, f'nasa_epic_{index}.png'),
            params,
        )


def main():

    load_dotenv()

    nasa_epic_url = os.environ['NASA_EPIC_URL']
    nasa_api_token = os.environ['NASA_API_TOKEN']
    images_directory = os.environ['IMAGES_DIRECTORY']

    create_directory(images_directory)

    nasa_request_params = {
        'api_key': nasa_api_token,
    }

    fetch_nasa_epic_images(
        nasa_epic_url,
        nasa_request_params,
        images_directory,
    )


if __name__ == '__main__':
    main()

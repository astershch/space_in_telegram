import datetime
import os

import requests

from pathlib import Path

from dotenv import load_dotenv

from download_helpers import download_image


def fetch_nasa_epic_images(params, directory):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    response = requests.get(nasa_epic_url, params=params)
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

    nasa_api_token = os.environ['NASA_API_TOKEN']
    images_directory = os.environ['IMAGES_DIRECTORY']

    Path(images_directory).mkdir(parents=True, exist_ok=True)

    nasa_request_params = {
        'api_key': nasa_api_token,
    }

    fetch_nasa_epic_images(
        nasa_request_params,
        images_directory,
    )


if __name__ == '__main__':
    main()

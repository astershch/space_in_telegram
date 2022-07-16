import argparse
import os
import random

import telegram

from dotenv import load_dotenv


def main():

    load_dotenv()

    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    images_directory = os.environ['IMAGES_DIRECTORY']
    images_directory = os.environ['TG_MAX_IMAGE_SIZE']

    bot = telegram.Bot(token=bot_token)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image',
        help='path to image, send specific image '
             'to telegram channel or random if None',
        nargs='?',
    )
    args = parser.parse_args()

    if args.image is not None:
        image = args.image_path
    else:
        images = []

        for root, dirs, files in os.walk(images_directory):
            for file in files:
                image = os.path.join(root, file)
                images.append(image)

        image = random.choice(images)

    with open(image, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    main()

import argparse
import os
import random

import telegram

from dotenv import load_dotenv


def choice_random_image(images_directory):
    images = []

    for root, dirs, files in os.walk(images_directory):
        for file in files:
            image = os.path.join(root, file)
            images.append(image)

    image = random.choice(images)

    return image


def main():

    load_dotenv()

    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    images_directory = os.environ['IMAGES_DIRECTORY']

    bot = telegram.Bot(token=bot_token)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image',
        help='path to image, send specific image '
             'to telegram channel or random if None',
        nargs='?',
    )
    args = parser.parse_args()

    if args.image:
        image = args.image
    else:
        image = choice_random_image(images_directory)

    with open(image, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    main()

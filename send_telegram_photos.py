import os
import random
import time

import telegram

from dotenv import load_dotenv


def send_photo_with_delay(bot, image, chat_id, publications_delay):
    with open(image, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

    time.sleep(3600 * publications_delay)


def main():

    load_dotenv()

    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    images_directory = os.environ['IMAGES_DIRECTORY']
    if os.getenv('TG_PUBLICATONS_DELAY') is None:
        publications_delay = 4
    else:
        publications_delay = int(os.getenv('TG_PUBLICATONS_DELAY'))

    bot = telegram.Bot(token=bot_token)

    images = []

    while True:

        for root, dirs, files in os.walk(images_directory):
            for file in files:
                image = os.path.join(root, file)

                if image not in images:
                    images.append(image)
                    send_photo_with_delay(
                        bot,
                        image,
                        chat_id,
                        publications_delay,
                    )

        else:
            image = random.choice(images)
            send_photo_with_delay(
                bot,
                image,
                chat_id,
                publications_delay,
            )


if __name__ == '__main__':
    main()

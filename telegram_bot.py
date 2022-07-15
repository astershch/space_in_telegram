import os

import telegram

from dotenv import load_dotenv


def main():

    load_dotenv()
    
    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']

    bot = telegram.Bot(token=bot_token)

    bot.send_message(text='Hi', chat_id=chat_id)


if __name__ == '__main__':
    main()

from telegram.ext import Updater, CommandHandler
import requests
import logging
import random
import os


TOKEN = 'your token here'
PORT = int(os.environ.get('PORT', 5000))

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Motivational Quotes Bot  \n\n' 
    + 'Use /quote to get a random motivational quote \n\n' 
    + 'Use /about for detail and Source code.')

def getQuote(update, context):
    API = 'https://type.fit/api/quotes'
    req = requests.get(API).json()
    quote = random.choice(req)
    for _k, v in quote.items():
        context.bot.send_message(chat_id=update.effective_chat.id, text=v)

def about(update, context):
    update.message.reply_text('This bot is made by Sameera Madushan \n\n' 
    + 'Github : https://github.com/sameera-madushan \n' 
    + 'Facebook : https://www.facebook.com/c2FtZWVyYW1hZHVzaGFu \n' 
    + 'Twitter : https://twitter.com/__sa_miya__ \n\n' 
    + 'Source Code : https://github.com/sameera-madushan/Motivational-Quotes-Telegram-Bot')


def main():
    updater = Updater('your token here', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", getQuote))

    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
    updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + your token here)
    updater.idle()

if __name__ == '__main__':
    main()
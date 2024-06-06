from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler
import os

# Get the environment variables
TOKEN = os.getenv('TOKEN')
URL = os.getenv('URL')

# Initialize the Flask app
app = Flask(__name__)

# Initialize the bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

# Define the start command handler
def start(update: Update, context):
    keyboard = [[InlineKeyboardButton(text="Play Guess the Color", web_app={"url": URL})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Guess the Color game!', reply_markup=reply_markup)

# Add the start command handler to the dispatcher
dispatcher.add_handler(CommandHandler('start', start))

# Define the webhook route
@app.route('/hook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Run the Flask app
if __name__ == '__main__':
    app.run(port=8443)

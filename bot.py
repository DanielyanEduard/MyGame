from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '6954506554:AAGkl8dF6w9xtsb3MscAsJvVLGYpBzZDHVM'

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton(text="Play Guess the Color", web_app={"url": "https://color-game.onrender.com"})]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the Guess the Color game!', reply_markup=reply_markup)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

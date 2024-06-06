from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR TOKEN HERE' with your bot's token
TOKEN = '6954506554:AAGkl8dF6w9xtsb3MscAsJvVLGYpBzZDHVM'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot. How can I help you?')

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

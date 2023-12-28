from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with the token you received from BotFather
TOKEN = 'YOUR_TOKEN'

# List of allowed user IDs
ALLOWED_USERS = [123456789, 987654321]  # Replace with your user IDs

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Photo Downloader Bot! Send /download to download the last photo.')

def download(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in ALLOWED_USERS:
        update.message.reply_text("Sorry, you are not allowed to use this bot.")
        return

    photo = update.message.photo[-1]  # Get the last (highest resolution) photo from the message
    file_id = photo.file_id
    file = context.bot.getFile(file_id)

    # Save the photo to a secure location or perform other operations
    file.download('downloaded_photo.jpg')

    update.message.reply_text('Photo downloaded successfully.')

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("download", download))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

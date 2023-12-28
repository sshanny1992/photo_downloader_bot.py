import os
import random
from flask import Flask, request
from telegram import Bot, Update

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

love_quotes = [
    "Love is not about how many days, months, or years you have been together. Love is about how much you love each other every single day.",
    "The best and most beautiful things in this world cannot be seen or even heard, but must be felt with the heart.",
    "Love is when the other person's happiness is more important than your own.",
    # Add more quotes here
]

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    update = Update.de_json(json_data, bot)
    handle_updates([update])
    return '', 200

def start(update):
    update.message.reply_text("Welcome to the Love Quotes Bot! Send /quote to get a random love quote.")

def quote(update):
    random_quote = random.choice(love_quotes)
    update.message.reply_text(random_quote)

def handle_updates(updates):
    for update in updates:
        if update.message and update.message.text:
            text = update.message.text.lower()
            if text.startswith('/start'):
                start(update)
            elif text.startswith('/quote'):
                quote(update)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))

from pyrogram import Client, filters
import asyncio

api_id = '27589257'
api_hash = '0af78b04b48361bc117fa4e06d6d2292'
bot_token = '7536811380:AAG5i2IIaGRRa_CGlfsErmTPGQtxCqR2VOc'

app = Client('spam_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

SPAM_MESSAGE = "🍅🍓🍆🍆🥑🍎🍍DICKHEAD 🍆🍆🍆☁️SUCK YOUR MOM🍌🍌🍌🍌🍆🍆🍆🍆🍆"
@app.on_message(filters.command('start') & filters.group)
async def start_spam(client, message):
    while True:
        try:
            await message.reply_text(SPAM_MESSAGE)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            break
app.run()

import os
import httpx
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")
IMAGE_URL = "https://i.postimg.cc/GhLnnLSw/1920h1080.png"

REPLY_TEXT = (
    '<tg-emoji emoji-id="5411126259965006700">👋</tg-emoji> Привет!\n\n'
    '<tg-emoji emoji-id="5408970607289208310">😊</tg-emoji> У нас позитивный чат: без ругани, рекламы и лишнего негатива\n\n'
    '<tg-emoji emoji-id="5418339700488311300">👇</tg-emoji> Полезные ссылки — ниже'
)

async def send_reply(chat_id, reply_to_message_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": IMAGE_URL,
        "caption": REPLY_TEXT,
        "parse_mode": "HTML",
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "5206217957297920049 Составы",
                        "url": "https://dota2.fandom.com/wiki/Category:Hero_minimap_icons",
                        "style": "primary"
                    },
                    {
                        "text": "5418003632182304206 Расписание",
                        "url": "https://www.hltv.org/events/9166/parken-challenger-championship-season-6",
                        "style": "success"
                    }
                ],
                [
                    {
                        "text": "5208844132230930228 Трансляция",
                        "url": "https://example.com",
                        "style": "danger"
                    }
                ]
            ]
        }
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.forward_from_chat and message.forward_from_chat.type == "channel":
        await send_reply(message.chat_id, message.message_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_channel_post))
app.run_polling()

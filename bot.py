import os
import httpx
import asyncio
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import Update

TOKEN = os.environ.get("TOKEN")
IMAGE_URL = "https://i.imgur.com/Hs6XKYX.png"
REPLY_TEXT = "👋 Привет! Вот полезные ссылки:"

async def send_reply(chat_id, reply_to_message_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    payload = {
        "chat_id": chat_id,
        "photo": IMAGE_URL,
        "caption": REPLY_TEXT,
        "reply_to_message_id": reply_to_message_id,
        "reply_markup": {
            "inline_keyboard": [
                [
                    {
                        "text": "📋 Составы",
                        "url": "https://dota2.fandom.com/wiki/Category:Hero_minimap_icons",
                        "style": "primary"
                    },
                    {
                        "text": "📅 Расписание",
                        "url": "https://www.hltv.org/events/9166/parken-challenger-championship-season-6",
                        "style": "success"
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

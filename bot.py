from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

REPLY_TEXT = """
👋 Привет! Вот полезные ссылки:
"""

keyboard = [
    [
        InlineKeyboardButton("📋 Составы", url="https://dota2.fandom.com/wiki/Category:Hero_minimap_icons"),
        InlineKeyboardButton("📅 Расписание", url="https://www.hltv.org/events/9166/parken-challenger-championship-season-6"),
    ]
]
reply_markup = InlineKeyboardMarkup(keyboard)

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.forward_from_chat and message.forward_from_chat.type == "channel":
        await message.reply_text(
            REPLY_TEXT,
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_channel_post))
app.run_polling()

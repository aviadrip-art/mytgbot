from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

REPLY_TEXT = """
👋 Привет! Вот полезные ссылки:
"""

# Две кнопки в ряд
keyboard = [
    [
        InlineKeyboardButton("📋 Составы", url="https://ССЫЛКА_НА_СОСТАВЫ"),
        InlineKeyboardButton("📅 Расписание", url="https://ССЫЛКА_НА_РАСПИСАНИЕ"),
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

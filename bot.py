from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

REPLY_MESSAGE = """
👋 Привет! Вот полезные ссылки:

🔗 Ссылка 1: https://example.com
📄 Ссылка 2: https://docs.example.com
"""

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if message and message.forward_from_chat and message.forward_from_chat.type == "channel":
        await message.reply_text(REPLY_MESSAGE)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_channel_post))
app.run_polling()

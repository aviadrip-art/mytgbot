import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message:
        return
    
    entities = message.entities or message.caption_entities or []
    
    for entity in entities:
        if entity.type == "custom_emoji":
            print(f"Кастомный эмодзи ID: {entity.custom_emoji_id}")
    
    if not any(e.type == "custom_emoji" for e in entities):
        print("Кастомных эмодзи не найдено в сообщении")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle_message))
app.run_polling()

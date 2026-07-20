import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Здравствуйте! Я бот сервиса "Master link". Выберите команду из меню, чтобы начать работу.')

async def place_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Пожалуйста, опишите вашу проблему для размещения заявки.')

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Мы — сервис по ремонту и связи с мастерами вашего города.')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Заявка отменена.')

if __name__ == '__main__':
    application = ApplicationBuilder().token(8630921066:AAH0p_hsSfLEIf8XwFmPA5A0kuOVrSoCa0k).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("place_request", place_request))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("cancel", cancel))
    
    application.run_polling()

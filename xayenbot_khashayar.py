
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Telegram user ID of "Khashayar"
AUTHORIZED_USER_ID = 99323517

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    await update.message.reply_text("سلام خشایار، پرویز اینجاست!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    msg = update.message.text.lower()
    if "سلام" in msg:
        await update.message.reply_text("سلام داداش خشایار! چطوری؟")
    else:
        await update.message.reply_text("پرویز اینجاست، آماده‌م! چی می‌خوای بدونی؟")

if __name__ == '__main__':
    import os
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    app.run_polling()

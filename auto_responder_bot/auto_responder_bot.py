import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables from .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Bot token not found. Make sure .env exists and BOT_TOKEN is set.")
print("✅ Token loaded successfully")



# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m your Auto-Responder Bot.")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a message and I will auto-reply.")

# Auto response handler
async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "hi" in text or "hello" in text:
        reply = "Hey! 😊"
    elif "bye" in text:
        reply = "Goodbye! 👋"
    elif "thank" in text:
        reply = "You're welcome! 🙌"
    else:
        reply = "I got your message: " + update.message.text
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
    print("🤖 Auto-Responder Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

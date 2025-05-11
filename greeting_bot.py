from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# Load token from .env
load_dotenv()

# Debug: Print token to make sure it's loaded
GREETING_TOKEN = os.getenv("GREETING_TOKEN")
if GREETING_TOKEN:
    print("Token loaded successfully")
else:
    print("Failed to load token")

# Command handlers
async def good_morning(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Good morning!")
    print("Sent 'Good morning!' message")

async def good_afternoon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Good afternoon!")
    print("Sent 'Good afternoon!' message")

async def good_night(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Good night!")
    print("Sent 'Good night!' message")

# Main function
def main():
    app = ApplicationBuilder().token(GREETING_TOKEN).build()

    app.add_handler(CommandHandler("morning", good_morning))
    app.add_handler(CommandHandler("afternoon", good_afternoon))
    app.add_handler(CommandHandler("night", good_night))

    # Start the bot with polling
    print("Bot is running...")
    app.run_polling()

# Run the main function
if __name__ == "__main__":
    main()

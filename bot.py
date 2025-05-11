from telegram.ext import ApplicationBuilder, CommandHandler
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
TOKEN = os.getenv('BOT_TOKEN')

# Define the start command handler
async def start(update, context):
    await update.message.reply_text('Hello! I am your first learning bot.')

# Set up the application and add the handler
app = ApplicationBuilder().token(TOKEN).build()

# Add the start command handler
app.add_handler(CommandHandler("start", start))

# Start polling
print("Bot is running...")
app.run_polling()


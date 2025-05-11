import os
from dotenv import load_dotenv

load_dotenv()

# Access token from environment
BOT_TOKEN = os.getenv("BOT_TOKEN")
GREETING_TOKEN = os.getenv("GREETING_TOKEN")

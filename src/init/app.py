from os import environ
from telegram.ext import Application
from src.model.bot_manager import BotManager

token = environ.get("BOT_TOKEN")

application = Application.builder().token(token).build()

bot = application.bot

botm = BotManager(application).build()
from telegram.ext import CommandHandler
from .app import botm, application
from .screens import load_screens
from .start import start, start_inner

load_screens()

botm.start_inner = start_inner

# application.job_queue.run_repeating(action, interval=60, first=1)

application.add_handler(CommandHandler("start", start), 0)
botm.add_handlers()

def run():
    print("Запрашивание...")
    application.run_polling(0.1)
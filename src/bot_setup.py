import os
import sys
import logging
from datetime import datetime
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gym_tracker import GymTracker
from src.exercise import Exercise
from texts import COMAND_TEXTS
from src.TOKEN import TOKEN

gym_tracker = GymTracker()

logging.getLogger('httpx').setLevel(logging.WARNING)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    # level=logging.DEBUG
)

application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMAND_TEXTS["IT"]["start"]
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMAND_TEXTS["IT"]["help"],
        parse_mode=ParseMode.HTML
    )

async def new_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/esercizio ", "").split(",")
    date = update.effective_message.date.date()
    date = datetime.strptime(str(date),"%Y-%m-%d").strftime("%d/%m/%Y")

    text_to_send = COMAND_TEXTS["IT"]["exerciseRegisteredSuccessfully"]

    try:
        name, record = text[0], text[1]
        exercise = Exercise(name, record, date, update.effective_user.id)
        exercise_already_registered = gym_tracker.write_exercise(exercise)

        if exercise_already_registered == True:
            text_to_send = COMAND_TEXTS["IT"]["exerciseAlreadyRegistered"]
    except:
        text_to_send = COMAND_TEXTS["IT"]["ERROR"]["EXERCISE_REGISTER_ERROR"]

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_to_send,
        parse_mode=ParseMode.HTML
    )

async def read_all_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=gym_tracker.read_all_exercises(update.effective_user.id),
        parse_mode=ParseMode.HTML
    )

async def delete_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    exercise_name = update.message.text.replace("/cancella ", "").strip()
    text_to_send = COMAND_TEXTS["IT"]["exerciseDeleted"]

    try:
        gym_tracker.delete_exercise(exercise_name, update.effective_user.id)
    except:
        text_to_send = COMAND_TEXTS["IT"]["ERROR"]["EXERCISE_DELETION_ERROR"]

    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = text_to_send,
        parse_mode=ParseMode.HTML
    )

async def reset_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gym_tracker.reset_all(update.effective_user.id)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMAND_TEXTS["IT"]["reset"],
        parse_mode=ParseMode.HTML
    )

if __name__ == '__main__':
    handlers = [CommandHandler('start', start), CommandHandler('help', help), 
                CommandHandler('esercizio', new_exercise), CommandHandler('registro', read_all_exercises),
                CommandHandler('reset', reset_all), CommandHandler('cancella', delete_exercise)]
    
    for handler in handlers:
        application.add_handler(handler)

    application.run_polling()
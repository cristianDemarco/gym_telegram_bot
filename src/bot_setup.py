import os
import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gym_tracker import Exercise, GymTracker
from src.command_texts import COMMAND_TEXTS
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
        text=COMMAND_TEXTS["IT"]["start"]
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMMAND_TEXTS["IT"]["help"]
    )

async def new_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/esercizio ", "").split(",")
    text_to_send = COMMAND_TEXTS["IT"]["exerciseRegisteredSuccessfully"]

    try:
        name, record = text[0], text[1]
        exercise = Exercise(name, record, update.effective_user.id)
        gym_tracker.add_exercise(exercise)
    except Exception as e:
        print(e)
        text_to_send = COMMAND_TEXTS["IT"]["ERROR"]["EXERCISE_REGISTER_ERROR"]

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_to_send
    )

async def read_all_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=gym_tracker.read_all_exercises(update.effective_user.id)
    )

async def reset_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gym_tracker.reset_all()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMMAND_TEXTS["IT"]["reset"]
    )

    #THE LAST THING YOU SHOULD DO IS SEND THE MESSAGE TO THE USER
    #IF SOMETHING BREAKS IN RESET_ALL(), YOU TELL TO THE USER THAT YOU HAVE EXECUTED THE COMMAND BUT YOU DIDN'T!


if __name__ == '__main__':

    handlers = [CommandHandler('start', start), CommandHandler('help', help), 
                CommandHandler('esercizio', new_exercise), CommandHandler('registro', read_all_exercises),
                CommandHandler('reset', reset_all)]
    
    for handler in handlers:
        application.add_handler(handler)

    application.run_polling()
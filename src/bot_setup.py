import os
import sys
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gym_tracker import Exercise, GymTracker
from src.command_texts import COMMAND_TEXTS

gym_tracker = GymTracker()

TOKEN = "5968259667:AAGOg31yeuifCPNlr6VdsdHpKnWtRAjy0qs"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
    # level=logging.DEBUG
)

application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMMAND_TEXTS["start"]
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMMAND_TEXTS["help"]
    )

async def new_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.replace("/esercizio ", "").split()
    text_to_send = COMMAND_TEXTS["exerciseRegisteredSuccessfully"]

    try:
        name, record = text[0], text[1]
        exercise = Exercise(name, record)
        gym_tracker.add_exercise(exercise)
    except:
        text_to_send = COMMAND_TEXTS["exerciseRegisteredUnsuccessfully"]

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text_to_send
    )

async def read_all_exercises(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=gym_tracker.read_all_exercises()
    )

async def reset_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=COMMAND_TEXTS["reset"]
    )

    gym_tracker.reset_all()


if __name__ == '__main__':
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    new_exercise_handler = CommandHandler('esercizio', new_exercise)
    read_all_exercises_handler = CommandHandler('registro', read_all_exercises)
    reset_all_handler = CommandHandler('reset', reset_all)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(new_exercise_handler)
    application.add_handler(read_all_exercises_handler)
    application.add_handler(reset_all_handler)

    application.run_polling()
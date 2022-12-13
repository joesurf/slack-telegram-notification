from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove



from pprint import pprint

import logging
import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



from database import create_db_connection

host = "localhost"
user = "dbadmin"
password = os.environ["DB_PASS"]
database = "teleslack"


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

DONE, CHECKING_CHOICE, WRONG_CHOICE = range(3)


def start(update: Update, context: CallbackContext):
    """
    
    """
    update.message.reply_text(
        "Welcome to The 100 Club Bot! Please type your email to verify your membership to The100Club.",
        # reply_markup=markup,
    )

    return CHECKING_CHOICE


def checking_choice(update: Update, context: CallbackContext) -> int:
    """
    
    """
    # Get identifier from user

    update.message.reply_text(
        "Checking email...",
    )

    identifier = update.message['text']
    chat_id = update.message.chat_id

    connection = create_db_connection(host, user, password, database)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Profile WHERE identifier = "{identifier}"')

    if cursor.fetchone():
        try:
            cursor.execute(f'UPDATE Profile SET chat_id="{chat_id}" WHERE identifier = "{identifier}"')
            connection.commit()
            connection.close() 

            update.message.reply_text(
                "You are now subscribed to our Slack notifications. :D",
            )
        except Exception as e:
            update.message.reply_text(
                "Oh no, there's a huge problem here. Please contact @joesurfrk for assistance.",
            )
        finally:
            return ConversationHandler.END

    else:
        connection.commit()
        connection.close()

        update.message.reply_text(
            "Oh no, there's a problem with this email. Please try again or contact @joesurfrk for assistance.",
        )

        return CHECKING_CHOICE


def done(update: Update, context: CallbackContext) -> int:
    """
    End the conversation
    """
    return ConversationHandler.END


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        Contact @joesurfrk for assistance
        """
    )


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)






def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    updater = Updater(
        os.environ["TELEGRAM_BOT_TOKEN"],
        use_context=True
    )

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHECKING_CHOICE: [
                MessageHandler(
                    filters.Filters.regex("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"), checking_choice
                ),
                # MessageHandler(
                #     filters.Filters.text & ~(filters.Filters.command | filters.Filters.regex("^Done$")), checking_choice
                # )            
            ],
        },
        fallbacks=[MessageHandler(filters.Filters.regex("^Done$"), done)],
    )

    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('help', help))
    
    # Filters out unknown commands
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    # Run the bot until the user presses Ctrl-C
    updater.start_polling()


if __name__ == "__main__":
    main()













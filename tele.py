from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



from database import create_db_connection

host = "localhost"
user = "root"
password = os.environ["DB_PASS"]
database = "teleslack"





# cursor.execute('SELECT * FROM Member WHERE MembershipID=%s', MembershipID_entry.get())
# row = cursor.fetchone()




updater = Updater(os.environ["TELEGRAM_BOT_TOKEN"],
    use_context=True)

def start(update: Update, context: CallbackContext):

    update.message.reply_text("Welcome to The 100 Club Bot!")

    connection = create_db_connection(host, user, password, database)
    cursor = connection.cursor()

    identifier = "jozlpidc@gmail.com"
    chat_id = ""

    cursor.execute(f'UPDATE Member SET chat_id= {chat_id} WHERE identifier = {identifier}')
    connection.commit()
    connection.close()
    
    print("Saved chat successfully")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        """
        /start -> Welcome to The100Club
        """
    )

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("gmail link here")
  
  
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("youtube link")
  
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("Your linkedin profile url")
  
  
def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks url here")
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))




updater.start_polling()
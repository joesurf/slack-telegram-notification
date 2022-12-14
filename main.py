

# Run slack and telegram bots
import os
import logging
import requests
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
import emoji

from slack_bolt import App
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

from database import create_db_connection



# Initialising credentials 
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

host = os.environ.get("DB_HOST")
user = "admin"
password = os.environ.get("DB_PASS") 
database = "teleslack"

counter = 0


# Initializes Slack app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


# Slack functions

def is_subscribed(slack_id):
    """
    Check database to see if user is subscribed
    :user
    return telegram chat id
    """

    connection = create_db_connection(host, user, password, database) 
    cursor = connection.cursor()

    cursor.execute(f'SELECT chat_id FROM Profile WHERE slack_id = "{slack_id}"')
    response = cursor.fetchone()

    connection.commit()
    connection.close()

    if response is not None and response[0] != "Unsubscribed":
        return response[0]
    else:
        return None


# Detect any message sent to user
@app.message("")
def detect_messages(message, ack, say, client):
    """
    Scan for all messages sent in Slack.
    Identify subscribed users in private channels
    """

    ack()
    print("Detecting messages...")

    sender_id = message["user"]
    sender = client.users_profile_get(user=sender_id)["profile"]["display_name"]
    channel = message["channel"]

    msg = message["text"]
    content = f"""
        You have a message from {sender} in Slack! {emoji.emojize('????')}\
        \nhttps://slack.com/app_redirect?channel={channel}
    """

    users = client.conversations_members(channel=channel)["members"]
    print(users)

    tele_subscribers = []

    for user in users: # note user is slack_id
        print(user)
        chat_id = is_subscribed(user)
        if chat_id is not None and sender_id != user:
            tele_subscribers.append(chat_id)
        
    send_telegram({"content": content, "subscribers": tele_subscribers, "message": msg})


# Triggered by message detector to send tele
def send_telegram(payload):
    """
    Upon trigger by detect message
    Send content of message to all identified users
    :subscribed_users -> list
    :message_content -> string
    """

    content = payload["content"]
    subscribers = payload["subscribers"]
    msg = payload["message"]

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    method = "sendMessage"

    connection = create_db_connection(host, user, password, database)
    cursor = connection.cursor()

    for subscriber in subscribers:
        tele_message = content
        cursor.execute(f'SELECT group_type FROM Profile WHERE chat_id = "{subscriber}"')
        group_type = cursor.fetchone()[0]
        
        print(group_type)

        if group_type == "test":
            tele_message += f"\n{msg}"

        response = requests.post(
            url=f"https://api.telegram.org/bot{token}/{method}",
            data={'chat_id': subscriber, 'text': tele_message}
        ).json()

        print(response)

    print("Sent successfully!")
    

def sendSlackNotification(email, status):
    app.client.chat_postMessage(channel="C03NP6E3DDG", text=f"{email} just {status} to teleslack bot! Hooya")
    print("Successfully notified")
    return




# Telegram functions

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

DONE, CHECKING_CHOICE, LEAVE = range(3)


def start(update: Update, context: CallbackContext):
    """
    """
    update.message.reply_text(
        "Welcome to The 100 Club Bot! Please type your email to verify your membership to The100Club.",
        # reply_markup=markup, 
    )
    
    return CHECKING_CHOICE


def leave(update: Update, context: CallbackContext):
    """
    """
    # Remove chat_id and replace with ex- to indicate
    chat_id = update.message.chat_id

    connection = create_db_connection(host, user, password, database)
    cursor = connection.cursor()

    cursor.execute(f'SELECT identifier FROM Profile WHERE chat_id = "{chat_id}"')
    identifier = cursor.fetchone()[0]

    cursor.execute(f'SELECT chat_id FROM Profile WHERE chat_id = "{chat_id}"')

    print("checking status")


    if cursor.fetchone():
        print("unsubscribe")
        cursor.execute(f'UPDATE Profile SET chat_id = "Unsubscribed" WHERE chat_id = "{chat_id}"')

    connection.commit()
    connection.close()

    update.message.reply_text(
        "We're sorry to see you leave. Please let us know how we can serve you better.",
        # reply_markup=markup, 
    )
    
    # Inform team
    sendSlackNotification(identifier, "unsubscribed")
    
    return ConversationHandler.END


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
    cursor.execute(f'SELECT identifier FROM Profile WHERE identifier = "{identifier}"')

    if cursor.fetchone():
        try:

            # Add telegram chat id to database
            cursor.execute(
                f'UPDATE Profile SET chat_id="{chat_id}" WHERE identifier = "{identifier}"')

            # Add alternate fields for A/B testing - if not empty add next number
            cursor.execute(
                f'SELECT COUNT(group_type) FROM Profile WHERE group_type IS NOT NULL')
            counter = cursor.fetchone()[0]

            group_type = "control" if counter % 2 == 1 else "test"

            cursor.execute(f'SELECT group_type FROM Profile WHERE identifier = "{identifier}"')

            if cursor.fetchone():
                cursor.execute(
                    f'UPDATE Profile SET group_type="{group_type}" WHERE identifier = "{identifier}"')

            connection.commit()
            connection.close()

            update.message.reply_text(
                "You are now subscribed to our Slack notifications. :D",
            )

            # Inform team
            sendSlackNotification(identifier, "subscribed")

        except Exception as e:
            print(e)
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
        "Oops, our bot doesn't understand what '%s' means" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Oops '%s' is not a valid command" % update.message.text)


def main() -> None:
    """
    Run the telegram bot.
    """
    # Create the Application and pass it your bot's token.
    updater = Updater(
        os.environ.get("TELEGRAM_BOT_TOKEN"),
        use_context=True
    )

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHECKING_CHOICE: [
                MessageHandler(
                    filters.Filters.regex(
                        "([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"), checking_choice
                ),
                # MessageHandler(
                #     filters.Filters.text & ~(filters.Filters.command | filters.Filters.regex("^Done$")), checking_choice
                # )
            ],
        },
        fallbacks=[MessageHandler(filters.Filters.regex("^Done$"), done)],
    )

    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('leave', leave))

    # Filters out unknown commands
    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    # Filters out unknown messages.
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

    # Run the bot until the user presses Ctrl-C
    updater.start_polling()


# For local testing
# Start your app
# if __name__ == "__main__":
#     main()
#     app.start(port=int(os.environ.get("PORT", 5002)))


# Deploy Flask app with Slack connection 
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)
main() 

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request) 
from slack_bolt import App
import requests

import os
from dotenv import load_dotenv
from pathlib import Path


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)




# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message(":wave:")
def say_hello(message, say):
    user = "U030GMTB01J" # message['user']
    say(f"Hi there, <@{user}>!")



def is_subscribed(user):
    """
    Check database to see if user is subscribed

    :user

    return telegram chat id
    """

    response = DATABASE_GET

    if response is not None:
        return response.chat_id
    else:
        return None




# Detect any message sent to user
@app.message("fire")
def detect_messages(message, say):
    """
    Scan for all messages sent in Slack.
    Identify subscribed users in private channels
    """

    content = message["content"]

    tele_subscribers = []

    for user in users:
        chat_id = is_subscribed(user)
        if chat_id is not None:
            tele_subscribers.append(chat_id)
        
    return content + chat_id


# Triggered by message detector to send tele
# @app.action()
def send_telegram(payload):
    """
    Upon trigger by detect message
    Send content of message to all identified users

    :subscribed_users -> list
    :message_content -> string
    """

    content = payload["content"]
    chat_id = payload["chat_id"]

    response = requests.post(
        url=f"https://api.telegram.org/bot{token}/{method}",
        data={'chat_id': chat_id, 'text': content}
    ).json()



# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5002)))

    
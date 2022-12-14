from slack_bolt import App
import requests

import os
from dotenv import load_dotenv
from pathlib import Path

from pprint import pprint


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


from database import create_db_connection



host = "localhost"
user = "root"
password = os.environ.get("DB_PASS") 
database = "teleslack"



# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


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

    if response is not None:
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



    sender = client.users_profile_get(user=message["user"])["profile"]["display_name"]

    channel = message["channel"]

    msg = message["text"]
    content = f"""
        You have a message from {sender} in Slack! \
        \n{msg[:20]}...\
        \n\nhttps://slack.com/app_redirect?channel={channel}"""


    users = client.conversations_members(channel=channel)["members"]
    print(users)

    tele_subscribers = []

    for user in users: # note user is slack_id
        print(user)
        chat_id = is_subscribed(user)
        if chat_id is not None:
            tele_subscribers.append(chat_id)
        
    send_telegram({"content": content, "subscribers": tele_subscribers})




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
    subscribers = payload["subscribers"]

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    method = "sendMessage"

    for subscriber in subscribers:
        response = requests.post(
            url=f"https://api.telegram.org/bot{token}/{method}",
            data={'chat_id': subscriber, 'text': content}
        ).json()

        print(response)

    print("Sent successfully!")
    



# Start your app
# if __name__ == "__main__":
#     app.start(port=int(os.environ.get("PORT", 5002)))



from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)
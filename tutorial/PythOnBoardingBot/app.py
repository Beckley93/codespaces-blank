 """Module providing Function printing python version."""
import logging
logging.basicConfig()
from slack_sdk import WebClient

# test.py
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
client = WebClient()
api_response = client.api_test()

from slack_sdk import WebClient

token = "xoxb-5481474039187-5875251104550-dkBzhtpuz92HctSJfr3Eze3D"
slack = WebClient(token=token)
message = {"channel": "starter-bot-test", "text": "test"}
slack.chat_postMessage(**message)

#Sending a message to Slack

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

try:
    response = client.chat_postMessage(channel='#random', text="Hello world!")
    assert response["message"]["text"] == "Hello world!"
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
    
#Uploading files to Slack

# We've changed the process for uploading files to Slack to be much easier 
# and straight forward. You can now just include a path to the file directly
# in the API call and upload it that way.

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

try:
    filepath="./tmp.txt"
    response = client.files_upload_v2(channel='C0123456789', file=filepath)
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
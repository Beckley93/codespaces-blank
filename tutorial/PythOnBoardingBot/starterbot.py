import os
import time
import re
#from slackclient import SlackClient

"""Module providing Function printing python version."""
import logging
logging.basicConfig()
from slack_sdk import WebClient
token = "xoxb-5481474039187-5875251104550-dkBzhtpuz92HctSJfr3Eze3D"
refresh_token= None
token_update_callback= None
client_id= "5481474039187.5878905123157"
client_secret= "c9366fbfa0e33f72fc36d952446fdc70"
proxies= None
#starterbot_socketmode = "xapp-1-A05RUSM3M4M-5919474104561-dcecdb4386677e13dd236605efcf69fbadf06be22bbc7470d8a6d72e0e36ba96"

# starter-bot-test 
#Channel ID: C05SR509S76

channel_id = "D05RXS7EA58"
# copy link to profile: https://slackbot-muj5930.slack.com/team/U05RR7D32G6
#bot
# member_id = U05RR7D32G6
# bot Channel ID:D05RXS7EA58
# email: botuser-T05E5DY155H-B05SLRYFS3A@slack-bots.com

# event invite link : https://join.slack.com/t/slackbot-muj5930/shared_invite/zt-236w4ja1z-IJ0eUePz_WSQJ4QcubcCLw
# test.py
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
client = WebClient()
api_response = client.api_test()

#SlackClient(token= "xoxb-5481474039187-5875251104550-dkBzhtpuz92HctSJfr3Eze3D", refresh_token=None, token_update_callback=None, client_id= "5481474039187.5878905123157", client_secret= "c9366fbfa0e33f72fc36d952446fdc70", proxies=None, **kwargs)
#SlackClient(token, refresh_token, token_update_callback, client_id, client_secret, proxies=None, **kwargs)
#slack_client = SlackClient(token, refresh_token, token_update_callback, client_id, client_secret, proxies=None, **kwargs)
# instantiate Slack client
slack_client = SLACK_BOT_TOKEN 
#
# SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
#slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = A05RUSM3M4M
starterbot_id = None

# Member ID: U05RR7D32G6
#Channel ID: D05RXS7EA58
SLACK_BOT_TOKEN='xoxb-5481474039187-5875251104550-dkBzhtpuz92HctSJfr3Eze3D'
# <meta name="slack-app-id" content="A05RUSM3M4M">
client_id=5481474039187.5878905123157

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "do"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    """
        Executes bot command if the command is known
    """
    # Default response is help text for the user
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    # Finds and executes the given command, filling in response
    response = None
    # This is where you start to implement more commands!
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
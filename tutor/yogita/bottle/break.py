# # get the correct channel id
# # for channel in channels['channels']:
# #     if channel['name'] == channel_name:
# #         channel_id = channel['id']
# # if channel_id == None:
# #     raise Exception("cannot find channel " + channel_name)

# # # get the history as follows: 
# # history = sc.api_call("channels.history", channel=channel_id)

# # # get all the messages from the history: 
# # messages = history['messages']

# # # Or reference them by ID, so in this case get the first message:
# # ids = messages[0]

# #!/usr/bin/python
# '''
# Script to count messages by user posted to a channel for a given date range.
# Install:
# # sudo pip install slackclient
# Also you will need to obtain a slack API token:
#     https://api.slack.com/docs/oauth-test-tokens
# Usage Example:
 
# # python SLACK_SEARCH_FROM=2016-11-01 SLACK_SEARCH_TO=2016-12-01 \
#          SLACK_CHANNEL_NAME=general SLACK_API_TOKEN=<token> \
#          slack-messages-by-user.py
# '''

# # slack_webhooks url
# # https://hooks.slack.com/services/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




# import os
# from datetime import datetime
# import slack 

# slack_token = os.environ["SLACK_API_TOKEN"]
# channel_name = os.environ["SLACK_CHANNEL_NAME"]
# date_from = os.environ["SLACK_SEARCH_FROM"]
# date_to = os.environ["SLACK_SEARCH_TO"]

# oldest = (datetime.strptime(date_from, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()
# latest = (datetime.strptime(date_to, "%Y-%m-%d") - datetime(1970, 1, 1)).total_seconds()

# sc = slack.sdk(slack_token)

# users_list = sc.api_call("users.list")
# users = {}
# for user in users_list['members']:
#     users[user['id']] = user['profile']['first_name'] + ' ' + user['profile']['last_name']

# channels = sc.api_call("channels.list")
# channel_id = None
# for channel in channels['channels']:
#     if channel['name'] == channel_name:
#         channel_id = channel['id']
# if channel_id == None:
#     raise Exception("cannot find channel " + channel_name)

# history = sc.api_call("channels.history", channel=channel_id, oldest=oldest, latest=latest)
# posts_by_user = {}

# for message in history['messages']:
#     if message['user'] in posts_by_user:
#         posts_by_user[users[message['user']]] += 1
#     else:
#         posts_by_user[users[message['user']]] = 1

# for user, count in posts_by_user.items():
#     print (user, 'posted', count, 'messages')


# # import os
# # import slack
# # # Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
# # from slack_sdk.web import WebClient
# # from slack_sdk.errors import SlackApiError

# # # WebClient insantiates a client that can call API methods
# # # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
# # client = WebClient(token="xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti")
# # # Store conversation history
# # conversation_history = []
# # # ID of the channel you want to send the message to
# channel_id = "C03HGMADR3L"

# try:
#     # Call the conversations.history method using the WebClient
#     # conversations.history returns the first 100 messages by default
#     # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
#     import pdb;pdb.set_trace()
#     result = client.conversations_history(channel=channel_id)
#     conversation_history = result.data["messages"]

#     # Print results
#     print("{} messages found in {}".format(len(conversation_history), id))

# except SlackApiError as e:
#     print("Error creating conversation: {}".format(e))


import os
import slack
import json
from time import sleep
CHANNEL = "C03HGMADR3L"
MESSAGES_PER_PAGE = 200
MAX_MESSAGES = 1000
from slack import WebClient

# init web client
client = WebClient(token=" xoxb-2023650115936-5056996501456-z37N8nCdoWefMqraunEa3Sti")

# get first page
page = 1
print("Retrieving page {}".format(page))
# import pdb; pdb.set_trace()
response = client.conversations_history(
    channel=CHANNEL,
    limit=MESSAGES_PER_PAGE
)
assert response["ok"]
messages_all = response['messages']

# get additional pages if below max message and if they are any
while len(messages_all) + MESSAGES_PER_PAGE <= MAX_MESSAGES and response['has_more']:
    page += 1
    print("Retrieving page {}".format(page))
    sleep(1)   # need to wait 1 sec before next call due to rate limits
    response = client.conversations_history(
        channel=CHANNEL,
        limit=MESSAGES_PER_PAGE,
        cursor=response['response_metadata']['next_cursor']
    )
    assert response["ok"]
    messages = response['messages']
    messages_all = messages_all + messages

print(
    "Fetched a total of {} messages from channel {}".format(
        len(messages_all),
        CHANNEL
))

#write the result to a file
with open('m.json', 'w', encoding='utf-8') as f:
  json.dump(
      messages_all, 
      f, 
      sort_keys=True, 
      indent=4, 
      ensure_ascii=False
    )



































import sys
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
from slack_sdk import WebClient
client = WebClient()
api_response = client.api_test()
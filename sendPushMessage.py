'''
import requests

userID = input('Enter userID: ')
message = input('Enter message: ')

headers = {
    'userID': userID,
    'message': message
}
r = requests.post('https://pushmessagevialine.herokuapp.com/', headers=headers)
print(r.elapsed.total_seconds())
print(r.headers)
#print(r.json())
'''

import json
import sys
import os

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage
)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)


text_message = TextSendMessage(text='Hello, world')
message = [{"type": "text", "text": "Hello, world"}]

@responses.activate
def push_text_message():
    responses.add(
        responses.POST,
        LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
        json={}, status=200
    )

    line_bot_api.push_message('U11e778e2425c196b6787ec04a198449f', text_message)

push_text_message()
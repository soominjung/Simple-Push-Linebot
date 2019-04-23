import os
import sys

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

# get channel_access_token from your environment variable
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)

#try:
line_bot_api.push_message('U11e778e2425c196b6787ec04a198449f', TextSendMessage(text='Hello World!'))
#except LineBotApiError as e:
#    print('e')

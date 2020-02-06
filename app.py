from flask import Flask, request, abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)

### Script start ###

from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = 'OCdT27Cd85yb9ivonS1jzp6c7CaUZapwgBj6bI7lS2nYTfWUT4cOpxUNdUudXlDeBoVwpXXAnd+7NZdCQq5zoMDGkRHuZjlmKveDWCD343Dw1YGz+mzWIUnwitO1sEeYbWR64YFtje08sBdXKaUxgwdB04t89/1O/w1cDnyilFU=
# Channel Secret
handler = WebhookHandler('7b967ad4b6bbf696aab670578527747d')

# 監聽所有來自 / 的 Post Request
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    reply_text =event.message.text

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
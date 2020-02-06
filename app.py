from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

app = Flask(__name__)

line_bot_api = LineBotApi('OCdT27Cd85yb9ivonS1jzp6c7CaUZapwgBj6bI7lS2nYTfWUT4cOpxUNdUudXlDeBoVwpXXAnd+7NZdCQq5zoMDGkRHuZjlmKveDWCD343Dw1YGz+mzWIUnwitO1sEeYbWR64YFtje08sBdXKaUxgwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7b967ad4b6bbf696aab670578527747d')


@app.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
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

app = Flask(__name__)

line_bot_api = LineBotApi('Gm72s0K6+Zpu3fRP4fUOo0WDsDXa48BWZpacMnQ8yqLgj8GAnTlnT7DBDrwuFKmVXMQ7wS0raMjbFQ7XR8Ct4MYyLDzMY54akIMzTp3CRFo/z82w51RLti1vhFme2hWS77xH062ppSIK3Yjqngt2/QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('564408c39d2e74bce3e1cf2aae3cc897')


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
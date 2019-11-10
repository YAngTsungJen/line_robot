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

line_bot_api = LineBotApi('NgkqK4Timw6Owb705bmMpEGBnJC3yhpolAGwkPB5T1ViG5Oie2a7F+Ugm9OduZWMXMQ7wS0raMjbFQ7XR8Ct4MYyLDzMY54akIMzTp3CRFqTp2JGPAhUkt5cGD5PoGQm8JBcbMPf32t2gO4XfVqFRgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5d1ed193ca6f5530b97349071db24ac2')


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
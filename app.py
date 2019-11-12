from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage
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
    msg = event.message.text
    r = '很抱歉你說什麼'

    if '給我貼圖' in msg:
        sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage)
        return


    if msg in ['hi', 'Hi']:
        r = 'hi'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'



        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= r))


if __name__ == "__main__":
    app.run()
import os
from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (
    ApiClient, Configuration, MessagingApi, ReplyMessageRequest, TextMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.exceptions import InvalidSignatureError

app = Flask(__name__)
# print(os)
from dotenv import load_dotenv

load_dotenv()

configuration = Configuration(
    access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
)

handler = WebhookHandler(
    os.getenv("LINE_CHANNEL_SECRET")
)

# print("TOKEN:", os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))
# print("SECRET:", os.environ.get("LINE_CHANNEL_SECRET"))

@app.route("/webhook", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=f"คุณส่งมาว่า: {event.message.text}")]
            )
        )

if __name__ == "__main__":
    # ✅ เปิด host='0.0.0.0' ให้ ngrok เข้าได้
    app.run(host='0.0.0.0', port=5001, debug=True)
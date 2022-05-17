
from cProfile import label
from email import message

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
def Confirm_Template():
    message = TemplateSendMessage(
        alt_text='身份選擇',
        template=ConfirmTemplate(
            text="請選擇你的身份",
            actions=[PostbackTemplateAction(
                label="父母",
                text="我的身份是父母",
                data="parents"
            ),
            MessageTemplateAction(
                label="小孩",
                text="我的身份是小孩",
                data="children"
            )
            ]
        )


    )
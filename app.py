from distutils.debug import DEBUG
from flask import Flask, request, abort
import sqlite3 as sql
import sqlite3
from sqlalchemy import column
import json
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import time
import threading
app = Flask(__name__)
USER_ID="Uf9c2ea14a1840f162831762795d6b29a"
# Channel Access Token
line_bot_api = LineBotApi('MOfsGyp9Wnhl1O8vB6tMIDEQ/N6McTCMaeAu10qoJGXlYyC+P/NyOqI+xUKoHEYz6AGopsjIf52XLm6KpJbEA6eWgMg2Ny7d/5FO8zHnXWgXVeurungLBMMyNw+p2M/I55+Khj8LrRyxaxWNBMFrfQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9a057cc478a1c94b4804044ffcc373d6')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    person = request.get_data(as_text=True)
    person = json.loads(person)
    # USER_ID=person['events'][0]['source']['userId']
    # print(USER_ID)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)
    #重複語句
    print("----Start----")
    person = request.get_data(as_text=True)
    person = json.loads(person)
    USER_ID=person['events'][0]['source']['userId']#獲取USER_ID
    #call postback
    msg = event.message.text#獲取使用者輸入

    if 'adult1' in msg:
        #message = Confirm_Template()
        message = TemplateSendMessage(
        alt_text='身份選擇',
        template=ConfirmTemplate(
            text="我該怎麼稱呼你呢?",
            actions=[PostbackTemplateAction(
                label="家長",
                text="家長",
                data="parents"
            ),
            MessageTemplateAction(
                label="小孩",
                text="小孩",
                data="children"
            )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, message)
    
    

    if 'adult2'in msg:
        message = TemplateSendMessage(
        alt_text='情境選擇',
        template=ConfirmTemplate(
            text="請問你的小孩年齡為何",
            actions=[PostbackTemplateAction(
                label="國中小",
                text="國中小",
                data="1"
            ),
            MessageTemplateAction(
                label="高中以上",
                text="高中以上",
                data="2"
            )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, message)
    #print(msg)
    
    
    if 'adult3'  in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='煩惱1',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='小孩拒絕溝通',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='是叛逆期到了嗎？'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='小孩沉迷於電動，不做功課',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='近視越來越深，不知道未來怎麼辦'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='小孩不吃正餐，只吃零食',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='真是不愛惜自己的身體！'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='小孩抱怨家事太多',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='是叛逆期到了嗎？'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='小孩夜不歸宿',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='是叛逆期到了嗎？'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    

    
    
    if 'adult4' in msg:
        message = TextSendMessage(text="請你描述事情發生的經過。")
        line_bot_api.reply_message(event.reply_token, message)
    

    if 'adult5' in msg:
        message = TextSendMessage(text="拔拔或馬馬可以避免用責罵的方式對待小孩，而是講道理的方式，告訴小孩你這樣會吃壞肚子喔! 會不舒服要去看醫生叔叔，而且不吃正餐吃零食可是會長胖又長不高的! 或是自訂一個吃零食的時段或區間，養成孩子只有那個時段能吃零食的習慣，這樣會比較好喔~(略略略)")
        line_bot_api.reply_message(event.reply_token, message)


    if 'adult6' in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='煩惱2',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='心情如何：被惹毛 🙄',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='真的是小屁孩'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='心情如何：傷心 😥',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='為什麼他就是不能體諒我'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='心情如何：無助 😣',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='我該怎麼做才好'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='心情如何：生氣😡	',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='˙7pupupu'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    

    if 'adult7' in msg:
        message = TextSendMessage(text="一件事或行為惹毛我們，代表在一段關係中，我們想要去改變或改善")
        line_bot_api.reply_message(event.reply_token, message)
   
    
    if 'adult8'  in msg:
        message = TemplateSendMessage(
        alt_text='結尾',
        template=ConfirmTemplate(
            text="經過梳理完後，你現在情緒如何?",
            actions=[PostbackTemplateAction(
                label="平復許多",
                text="跟孩子好好談談吧",
                data="gift1"
            ),
            MessageTemplateAction(
                label="還是有點氣",
                text="退一步海闊天空",
                data="gift2"
            )
            ]
            )
        )
        #line_bot_api.push_message(push_token, 訊息物件)
        line_bot_api.reply_message(event.reply_token, message)
    

    if 'adult9' in msg:
        message = TemplateSendMessage(
        alt_text='結尾',
        template=ConfirmTemplate(
            text="是否要送孩子一個禮物呢？",
            actions=[PostbackTemplateAction(
                label="好",
                text="打開LINE商城，https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9",
                data="gift1"
            ),
            MessageTemplateAction(
                label="不要",
                text="找時間面對面好好溝通吧",
                data="gift2"
            )
            ]
            )
        )
        #line_bot_api.push_message(push_token, 訊息物件)
        line_bot_api.reply_message(event.reply_token, message)
    


   
    

    if 'adult-10'in msg:
        message = TextSendMessage(text="是否想要對孩子說些什麼? 範例：『!想說的話』")
        line_bot_api.reply_message(event.reply_token, message)
     




    if 'child1' in msg:
        message = TemplateSendMessage(
        alt_text='身份選擇',
        template=ConfirmTemplate(
            text="我該怎麼稱呼你呢?",
            actions=[PostbackTemplateAction(
                label="家長",
                text="家長",
                data="parents"
            ),
            MessageTemplateAction(
                label="小孩",
                text="小孩",
                data="children"
            )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, message)
    
    
    if 'child2'in msg:
        message = TemplateSendMessage(
        alt_text='情境選擇',
        template=ConfirmTemplate(
            text="請問你的年齡為何OuO?",
            actions=[PostbackTemplateAction(
                label="國中小",
                text="國中小",
                data="1"
            ),
            MessageTemplateAction(
                label="高中以上",
                text="高中以上",
                data="2"
            )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, message)
    print(msg)

    if 'child3'  in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='煩惱1',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='你不想和爸媽溝通',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='爸媽好煩...'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='不想寫功課，只想玩電動',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='打遊戲好快樂，熬夜感覺身體輕飄飄的'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='正餐不好吃，零食好吃多了',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='好甜好甜好甜好甜好甜呀呀呀呀咿呀~~~'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='為什麼回家要做家事（怒',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='哎，怎麼那麼命苦呢QAQ'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='被限制回家時間好討厭',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='我想去朋友家過夜辣....'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    if 'child4' in msg:
        message = TextSendMessage(text="請你描述事情發生的經過。")
        line_bot_api.reply_message(event.reply_token, message)
    

    if 'child5' in msg:
        message = TextSendMessage(text="媽媽很辛苦的在廚房煮飯，就是要讓你吃得健康呀～吃正餐可以攝取更均勻的營養素，會長高高也不會變胖喔！要珍惜媽媽的愛呀！")
        line_bot_api.reply_message(event.reply_token, message)


    if 'child6' in msg:
        carousel_template_message = TemplateSendMessage(
            alt_text='煩惱2',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='心情如何：被惹毛 🙄',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='啊啊啊啊啊啊啊啊啊啊啊'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='心情如何：傷心 😥',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='Q_Q'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='心情如何：無助 😣',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='怎麼辦怎麼辦怎麼辦'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    ),CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='心情如何：生氣😡	',
                        text=' ',
                        actions=[
                            MessageAction(
                                label='選擇',
                                text='˙7pupupu'
                            ),
                            URIAction(
                                label=' ',
                                uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    
    

    if 'child7' in msg:
        message = TextSendMessage(text="一件事或行為惹毛我們，代表在一段關係中，我們想要去改變或改善")
        line_bot_api.reply_message(event.reply_token, message)
   

    if 'child8'  in msg:
        message = TemplateSendMessage(
        alt_text='結尾',
        template=ConfirmTemplate(
            text="經過梳理完後，你現在情緒如何?",
            actions=[PostbackTemplateAction(
                label="平復許多",
                text="跟爸媽聊聊吧",
                data="gift1"
            ),
            MessageTemplateAction(
                label="還是有點氣",
                text="哼，我才不是那麼小氣的人呢",
                data="gift2"
            )
            ]
            )
        )
        #line_bot_api.push_message(push_token, 訊息物件)
        line_bot_api.reply_message(event.reply_token, message)
    

    if 'child9' in msg:
        message = TemplateSendMessage(
        alt_text='結尾',
        template=ConfirmTemplate(
            text="要不要送父母一個禮物呢？",
            actions=[PostbackTemplateAction(
                label="好",
                text="打開LINE商城，https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9",
                data="gift1"
            ),
            MessageTemplateAction(
                label="不要",
                text="找時間面對面好好溝通吧",
                data="gift2"
            )
            ]
            )
        )
        #line_bot_api.push_message(push_token, 訊息物件)
        line_bot_api.reply_message(event.reply_token, message)
    


   
    

    if 'child-10'in msg:
        message = TextSendMessage(text="是否想要對爸媽說些什麼? 範例：『!想說的話』")
        line_bot_api.reply_message(event.reply_token, message)



    if 'read' in msg:
        con = sql.connect("database.db")
        con.row_factory = sql.Row

        cur = con.cursor()
        cur.execute("select msg from parents")

        
        rows = cur.fetchall();
        for row in rows:
            print(row)
            say=row
        print(type(say))
        #row = row[1:]
        print(say)
        for i in say:
            print(i)
            i=i[1:]
        # row = json.loads(row[1:])
        message = TextSendMessage(text=i)
        print(message)
        line_bot_api.push_message(USER_ID, message)

    if '!' in msg:
        print("Handle: reply_token: " + event.reply_token + ", message: " + event.message.text)
        message = TextSendMessage(text="留言已紀錄，可使用read讀取")
        print(message.text)

        try:
          with sql.connect("database.db") as con:
             cur = con.cursor()

             cur.execute("INSERT INTO parents (ID,msg) VALUES (?,?)",("1",event.message.text) )

             con.commit()
             msg = "Record successfully added"
             print(msg)
        except:
          con.rollback()
          msg = "error in insert operation"
          print(msg)

        finally:
            con.close()

        line_bot_api.reply_message(event.reply_token, message)
        print("-----------")

        






    # time.sleep(4)
    # message = TemplateSendMessage(
    #     alt_text='身份選擇',
    #     template=ConfirmTemplate(
    #         text="我該怎麼稱呼你呢?",
    #         actions=[PostbackTemplateAction(
    #             label="家長",
    #             text="家長",
    #             data="parents"
    #         ),
    #         MessageTemplateAction(
    #             label="小孩",
    #             text="小孩",
    #             data="children"
    #         )
    #         ]
    #     )
    # )
    # line_bot_api.push_message(USER_ID,message)
    

    # time.sleep(5)
    # message = TemplateSendMessage(
    #     alt_text='情境選擇',
    #     template=ConfirmTemplate(
    #         text="請問你的年齡為何OuO?",
    #         actions=[PostbackTemplateAction(
    #             label="國中小",
    #             text="國中小",
    #             data="1"
    #         ),
    #         MessageTemplateAction(
    #             label="高中以上",
    #             text="高中以上",
    #             data="2"
    #         )
    #         ]
    #     )
    # )
    # line_bot_api.push_message(USER_ID,message)
    # print(msg)

    # time.sleep(6)
    # carousel_template_message = TemplateSendMessage(
    #         alt_text='煩惱1',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
    #                     title='你不想和爸媽溝通',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='爸媽好煩...'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
    #                     title='不想寫功課，只想玩電動',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='打遊戲好快樂，熬夜感覺身體輕飄飄的'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
    #                     title='正餐不好吃，零食好吃多了',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='好甜好甜好甜好甜好甜呀呀呀呀咿呀~~~'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
    #                     title='為什麼回家要做家事（怒',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='哎，怎麼那麼命苦呢QAQ'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
    #                     title='被限制回家時間好討厭',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='我想去朋友家過夜辣....'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 )
    #             ]
    #         )
    #     )
    # line_bot_api.push_message(USER_ID,carousel_template_message)
    
    # time.sleep(6)
    # message = TextSendMessage(text="請你描述事情發生的經過。")
    # line_bot_api.push_message(USER_ID,message)
    
    # time.sleep(5)
    # message = TextSendMessage(text="媽媽很辛苦的在廚房煮飯，就是要讓你吃得健康呀～吃正餐可以攝取更均勻的營養素，會長高高也不會變胖喔！要珍惜媽媽的愛呀！")
    # line_bot_api.push_message(USER_ID,message)


    # time.sleep(1)
    # carousel_template_message = TemplateSendMessage(
    #         alt_text='煩惱',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
    #                     title='心情如何：被惹毛 🙄',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='啊啊啊啊啊啊啊啊啊啊啊'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
    #                     title='心情如何：傷心 😥',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='Q_Q'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
    #                     title='心情如何：無助 😣',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='怎麼辦怎麼辦怎麼辦'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 ),CarouselColumn(
    #                     thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
    #                     title='心情如何：生氣😡	',
    #                     text=' ',
    #                     actions=[
    #                         MessageAction(
    #                             label='選擇',
    #                             text='˙7pupupu'
    #                         ),
    #                         URIAction(
    #                             label=' ',
    #                             uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
    #                         )
    #                     ]
    #                 )
    #             ]
    #         )
    #     )
    # line_bot_api.push_message(USER_ID,carousel_template_message)
    
    
    # time.sleep(1)
    # message = TextSendMessage(text="一件事或行為惹毛我們，代表在一段關係中，我們想要去改變或改善")
    # line_bot_api.push_message(USER_ID,message)   


    # time.sleep(1)
    # message = TemplateSendMessage(
    #     alt_text='結尾',
    #     template=ConfirmTemplate(
    #         text="經過梳理完後，你現在情緒如何?",
    #         actions=[PostbackTemplateAction(
    #             label="平復許多",
    #             text="跟爸媽聊聊吧",
    #             data="gift1"
    #         ),
    #         MessageTemplateAction(
    #             label="還是有點氣",
    #             text="哼，我才不是那麼小氣的人呢",
    #             data="gift2"
    #         )
    #         ]
    #         )
    #     )
    #     #line_bot_api.push_message(push_token, 訊息物件)
    # line_bot_api.push_message(USER_ID,message)

    # time.sleep(1)
    # message = TemplateSendMessage(
    #     alt_text='結尾',
    #     template=ConfirmTemplate(
    #         text="要不要送父母一個禮物呢？",
    #         actions=[PostbackTemplateAction(
    #             label="好",
    #             text="打開LINE商城，https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9",
    #             data="gift1"
    #         ),
    #         MessageTemplateAction(
    #             label="不要",
    #             text="找時間面對面好好溝通吧",
    #             data="gift2"
    #         )
    #         ]
    #         )
    #     )
    #     #line_bot_api.push_message(push_token, 訊息物件)
    # line_bot_api.push_message(USER_ID,message)    


   
    
    # time.sleep(1)

    # message = TextSendMessage(text="是否想要對爸媽說些什麼? 範例：『!想說的話』")
    # line_bot_api.push_message(USER_ID,message)    
    













     # print(request.get_data(as_text=True))

        # person = request.get_data(as_text=True)
        # person = json.loads(person)
        # USER_ID=person['events'][0]['source']['userId']

    # if 'user' in msg:
    #     person = request.get_data(as_text=True)
    #     person = json.loads(person)
    #     USER_ID=person['events'][0]['source']['userId']
    #     print(USER_ID)
    # if 'push' in msg:
        
    #     line_bot_api.push_message('U80310c1cc3d9f4d0c171350b3fd37b43', TextSendMessage(text='Hello World!'))
















@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
       try:
          nm = request.form['nm']
          addr = request.form['add']
          city = request.form['city']
          pin = request.form['pin']

          with sql.connect("database.db") as con:
             cur = con.cursor()

             cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )

             con.commit()
             msg = "Record successfully added"
       except:
          con.rollback()
          msg = "error in insert operation"

       finally:
            con.close()
            return None

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return None



@app.route('/initP')
def initP():
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE parents (ID TEXT, msg TEXT)')
    print ("Table created successfully")
    return None
    conn.close()


@app.route('/initC')
def initC():
    conn = sqlite3.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE children (ID TEXT, msg TEXT)')
    print ("Table created successfully")
    return None
    conn.close()


# time.sleep(6)

# message = TemplateSendMessage(
#     alt_text='身份選擇',
#     template=ConfirmTemplate(
#         text="我該怎麼稱呼你呢?",
#         actions=[PostbackTemplateAction(
#             label="家長",
#             text="我是家長",
#             data="parents"
#         ),
#         MessageTemplateAction(
#             label="小孩",
#             text="我是小孩",
#             data="children"
#         )
#         ]
#     )
# )
# line_bot_api.push_message(USER_ID,message)

# time.sleep(6)

# message = TemplateSendMessage(
#     alt_text='情境選擇',
#     template=ConfirmTemplate(
#         text="請選擇你的情境",
#         actions=[PostbackTemplateAction(
#             label="國中小",
#             text="國中小",
#             data="1"
#         ),
#         MessageTemplateAction(
#             label="高中以上",
#             text="高中以上",
#             data="2"
#         )
#         ]
#     )
#     )
# line_bot_api.push_message(USER_ID,message)

# time.sleep(6)

# carousel_template_message = TemplateSendMessage(
#         alt_text='煩惱1',
#         template=CarouselTemplate(
#                 columns=[
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
#                         title='小孩拒絕溝通',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='是叛逆期到了嗎？'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
#                         title='小孩沉迷於電動，不做功課',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='近視越來越深，不知道未來怎麼辦'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
#                         title='小孩不吃正餐，只吃零食',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='真是不愛惜自己的身體！'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     )
#                 ]
#             )
#         )
# line_bot_api.push_message(USER_ID,carousel_template_message)

# time.sleep(6)

# message = TextSendMessage(text="請你描述事情發生的經過")
# line_bot_api.push_message(USER_ID,message)


# time.sleep(6)

# carousel_template_message = TemplateSendMessage(
#             alt_text='煩惱2',
#             template=CarouselTemplate(
#                 columns=[
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
#                         title='被惹毛 🙄',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='真的是小屁孩'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
#                         title='傷心 😥',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='為什麼他就是不能體諒我'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     ),
#                     CarouselColumn(
#                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
#                         title='無助 😣',
#                         text=' ',
#                         actions=[
#                             MessageAction(
#                                 label='選擇',
#                                 text='我該怎麼做才好'
#                             ),
#                             URIAction(
#                                 label=' ',
#                                 uri='https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9'
#                             )
#                         ]
#                     )
#                 ]
#             )
#         )
# line_bot_api.push_message(USER_ID,carousel_template_message)

# time.sleep(6)

# message = TextSendMessage(text="一件事或行為惹毛我們，代表在一段關係中，我們想要去改變或改善")
# line_bot_api.push_message(USER_ID,message)


# time.sleep(6)

# message = TemplateSendMessage(
#     alt_text='結尾',
#     template=ConfirmTemplate(
#         text="經過梳理完後，你現在情緒如何?",
#             actions=[PostbackTemplateAction(
#                 label="平復許多",
#                 text="跟孩子好好談談吧",
#                 data="gift1"
#             ),
#             MessageTemplateAction(
#                 label="還是有點氣",
#                 text="退一步海闊天空",
#                 data="gift2"
#             )
#             ]
#             )
#         )
# line_bot_api.push_message(USER_ID,message)

# time.sleep(6)

# message = TemplateSendMessage(
#         alt_text='結尾',
#         template=ConfirmTemplate(
#             text="是否要給父母（孩子）送個禮物呢？",
#             actions=[PostbackTemplateAction(
#                 label="好",
#                 text="打開LINE商城，https://lineshopping.page.link/dMrY4ii9Tc7FAWbv9",
#                 data="gift1"
#             ),
#             MessageTemplateAction(
#                 label="不要",
#                 text="找時間面對面好好溝通吧",
#                 data="gift2"
#             )
#             ]
#             )
#         )
#         #line_bot_api.push_message(push_token, 訊息物件)
# line_bot_api.push_message(USER_ID,message)

# time.sleep(6)
# message = TextSendMessage(text="是否想要對孩子說些什麼? 範例：『!想說的話』")
# line_bot_api.push_message(USER_ID,message)   


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=5000 ,debug=True)

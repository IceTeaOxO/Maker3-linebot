from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('MOfsGyp9Wnhl1O8vB6tMIDEQ/N6McTCMaeAu10qoJGXlYyC+P/NyOqI+xUKoHEYz6AGopsjIf52XLm6KpJbEA6eWgMg2Ny7d/5FO8zHnXWgXVeurungLBMMyNw+p2M/I55+Khj8LrRyxaxWNBMFrfQdB04t89/1O/w1cDnyilFU=')

with open("1.png", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-702e615675f7985eff8d72afd3468060", "image/jpeg", f)
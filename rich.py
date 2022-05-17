import requests
import json

headers = {"Authorization":"Bearer MOfsGyp9Wnhl1O8vB6tMIDEQ/N6McTCMaeAu10qoJGXlYyC+P/NyOqI+xUKoHEYz6AGopsjIf52XLm6KpJbEA6eWgMg2Ny7d/5FO8zHnXWgXVeurungLBMMyNw+p2M/I55+Khj8LrRyxaxWNBMFrfQdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "Controller",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 1250, "height": 834},
          "action": {"type": "message", "text": "read"}
        },
        {
          "bounds": {"x": 0, "y": 834, "width": 1250, "height": 834},
          "action": {"type": "message", "text": "!文字：將文字儲存進資料庫，read：讀取資料，demo1~9：範例展示"}
        },
        {
          "bounds": {"x": 1250, "y": 0, "width": 1250, "height": 834},
          "action": {"type": "message", "text": "demo8"}
        },
        {
          "bounds": {"x": 1250, "y": 834, "width": 1250, "height": 834},
          "action": {"type": "message", "text": "demo1"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', 
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)
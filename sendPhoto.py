import requests
from pprint import pprint

TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'

def sendPhoto(chat_id:int, photo:str):
    Basic_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params = {
        'chat_id':chat_id,
    }
    fies = {
        'photo':photo
    }

    response = requests.post(url= Basic_url, params=params,files=fies)
    data = response.json()
    return data

photo_url = 'https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
photo_id = 'AgACAgIAAxkBAAIC4mPoz7KKdPf3q2jGwze9U4__UIysAAL4xTEb-udJSz6xtcwlBJF8AQADAgADeQADLgQ'
logo = open('logo.jpg','rb').read()
chat_id = 996172963

if __name__=='__main__':
    pprint(sendPhoto(chat_id=chat_id, photo=logo))

import requests
from pprint import pprint

TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'

def sendPhoto(chat_id:int, photo_url:str):
    Basic_url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    params = {
        'chat_id':chat_id,
        'photo':photo_url
    }

    response = requests.post(url= Basic_url, params=params)
    data = response.json()
    return data

photo_url = 'https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'
chat_id = 996172963

if __name__=='__main__':
    pprint(sendPhoto(chat_id=chat_id, photo_url=photo_url))

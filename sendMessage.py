import requests
from pprint import pprint

def sendMessage(chat_id:str, text:str):
    TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'
    Basic_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        'chat_id':chat_id,
        'text':text,
        'parse_mode':"MarkdownV2"
    }

    response = requests.post(url=Basic_url, data=payload)
    data = response.json()
    return data

if __name__=='__main__':
    pprint(sendMessage(chat_id=996172963, text='**Hello** , *hello* , _hello_ , __hello__ , ||hello||'))
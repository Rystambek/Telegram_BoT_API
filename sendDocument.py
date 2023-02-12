import requests
from pprint import pprint

TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'

def sendDocument(chat_id:str, doc_id:str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    data = {
        "chat_id":chat_id
    }

    files = {
        "document":doc_id
    }

    response = requests.post(url=url, params=data, files=files)
    data = response.json()
    return data

doc = open("sendPhoto.py",'rb').read()
id = 996172963
if __name__=="__main__":
    print(sendDocument(chat_id=id, doc_id=doc))
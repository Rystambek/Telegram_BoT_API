import requests
from pprint import pprint

def getUpdates()->dict:
    TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'
    basic_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url=basic_url)
    data = response.json()
    return data['result']
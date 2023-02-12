import requests
from pprint import pprint

def getMe()->dict:
    TOKEN = '5455890832:AAGh9-yUlkri7iXD5V4AOlWDdRN-pAiOBLY'
    Basic_url = f"https://api.telegram.org/bot{TOKEN}/getMe"
    response = requests.get(url=Basic_url)
    data = response.json()
    return data

pprint(getMe())

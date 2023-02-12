from getUpdates import getUpdates
from sendMessage import sendMessage
from main import randomDog
from sendPhoto import sendPhoto
from time import sleep

last_update_id = -1

while True:
    data = getUpdates()
    update_id = data[-1]['update_id']
    chat_id = data[-1]['message']['chat']['id']
    text = data[-1]['message']['text']

    print(text, chat_id)
    if update_id != last_update_id:
        if text == '/start':
            photo = randomDog()
            sendPhoto(chat_id=chat_id, photo=photo)
        else:
            sendMessage(chat_id=chat_id, text=text)#'||Rystambek akang kuchaydi Uji||')
        last_update_id = update_id

        sleep(2)
import requests

def randomDog():
    response = requests.get('https://random.dog/woof.json')
    data = response.json()['url']

    return data

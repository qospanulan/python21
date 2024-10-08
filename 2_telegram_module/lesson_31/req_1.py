import requests


def send_message(token, text, chat_id):

    # url = 'https://httpbin.org/image/jpeg'

    # token = '7800185758:AAEkd4LIRIDvO53CKy4Orueht8SyUJNgxBo'
    # url = f'https://api.telegram.org/bot{token}/getUpdates'
    # 6179607626 - Ulan
    # 514444384 - Vladimir
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

    response = requests.get(url)

    print(response.content)


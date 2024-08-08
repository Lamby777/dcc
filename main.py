#!/usr/bin/env python
import requests

DYNMAP_TARGET = input(
    "Enter the target domain and also port if applicable (e.g. 'solarsystem.coffee:5004'):\n"
)
USE_HTTPS = input('Use HTTPS? (y/n)\n').lower() == 'y'

url = f'http{"s" if USE_HTTPS else ""}://{DYNMAP_TARGET}/up/sendmessage'


def packet_data(message):
    return {'name': '', 'message': message}


def headers(message):
    return {
        'Host': DYNMAP_TARGET,
        'Connection': 'keep-alive',
        'Content-Length': str(len(message)),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Sec-GPC': '1',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': f'http://{DYNMAP_TARGET}',
        'Referer': f'http://{DYNMAP_TARGET}/',
        'Accept-Encoding': 'gzip, deflate',
        # 'Cookie': 'JSESSIONID=node08yt0udk45lbwcniyufccce8r35.node0'
    }


while True:
    try:
        message = input('Enter message: ')
    except (EOFError, KeyboardInterrupt):
        break

    response = requests.post(
        url, headers=headers(message), json=packet_data(message)
    )

    if response.status_code != 200:
        print('Error: ' + str(response.status_code))
        print(response.text)

    if response.json()['error'] != 'none':
        print('Error: ' + response.json()['error'])

    print('')

print('\n\nGoodbye!')

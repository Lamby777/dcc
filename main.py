import requests

url = 'http://solarsystem.coffee:5004/up/sendmessage'

def packet_data(message):
    return {
        "name": "",
        "message": message
    }

def headers(message):
    return {
        'Host': 'solarsystem.coffee:5004',
        'Connection': 'keep-alive',
        'Content-Length': str(len(message)),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Sec-GPC': '1',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'http://solarsystem.coffee:5004',
        'Referer': 'http://solarsystem.coffee:5004/',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'JSESSIONID=node08yt0udk45lbwcniyufccce8r35.node0'
    }


while True:
    try:
        message = input("Enter message: ")
    except KeyboardInterrupt:
        break

    response = requests.post(url, headers=headers(message), json=packet_data(message))

    print(response.status_code)
    print(response.text)
    print("")

print("\n\nGoodbye!")

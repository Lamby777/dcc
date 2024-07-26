
import requests

url = 'http://solarsystem.coffee:5004/up/sendmessage'
headers = {
    'Host': 'solarsystem.coffee:5004',
    'Connection': 'keep-alive',
    'Content-Length': '36',
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
data = {
    "name": "",
    "message": "i'm sending all of these by editing a string in the code and running the script btw"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)

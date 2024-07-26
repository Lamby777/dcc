import socket

def create_request(message):
    host = 'solarsystem.coffee'
    port = 5004
    payload = f'{{"name":"","message":"{message}"}}'
    headers = f"""POST /up/sendmessage HTTP/1.1\r
Host: {host}:{port}\r
Connection: keep-alive\r
Content-Length: {len(payload)}\r
Accept: application/json, text/javascript, */*; q=0.01\r
DNT: 1\r
X-Requested-With: XMLHttpRequest\r
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\r
Content-Type: application/json; charset=UTF-8\r
Sec-GPC: 1\r
Accept-Language: en-US,en;q=0.5\r
Origin: http://{host}:{port}\r
Referer: http://{host}:{port}/\r
Accept-Encoding: gzip, deflate\r
Cookie: JSESSIONID=node08yt0udk45lbwcniyufccce8r35.node0\r
\r
{payload}"""
    return headers, payload

def send_message(message):
    host = 'solarsystem.coffee'
    port = 5004

    headers, payload = create_request(message)
    request = headers

    # Create a socket and connect
    with socket.create_connection((host, port)) as sock:
        # Send the request
        sock.sendall(request.encode())

        # Receive the response
        response = sock.recv(4096)
        print(response.decode())

# Example usage
send_message("123")

# while True:
#     try:
#         message = input("Enter message: ")
#     except (EOFError, KeyboardInterrupt):
#         break
#
#     # response = requests.post(url, headers=headers(message), json=packet_data(message))
#     s.sendall(headers(message).encode())
#     print(s.recv(1024))
#
#     # if response.status_code != 200:
#     #     print("Error: " + str(response.status_code))
#     #     print(response.text)
#     #
#     # if response.json()["error"] != "none":
#     #     print("Error: " + response.json()["error"])
#
#     print("")
#
# print("\n\nGoodbye!")

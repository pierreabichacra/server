import requests
import socketserver
import http.server
import ssl
import json


# https://api.telegram.org/bot5344382469:AAH3_q0O_dzTL4zDNTIHQG9Qax7ldW6FDig/setWebHook?url=167.235.254.139:8443

def getResponse(user_input):
    return user_input

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print("got a post")
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        json_data = json.loads(post_data)

        chat_id = json_data['message']['from']['id']
        user_input = json_data['message']['text']

        bot_output = getResponse(user_input) 
        url = "https://api.telegram.org/bot5344382469:AAH3_q0O_dzTL4zDNTIHQG9Qax7ldW6FDig/sendMessage"
        r = requests.post(url = url, params = {'chat_id' : chat_id, 'text': bot_output})
        if r.status_code == 200:
            self.send_response(200)
            self.end_headers()
        

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        

server = socketserver.TCPServer(('0.0.0.0', 8443), MyHandler)
import socket 
print('listening on ', socket.gethostbyname(socket.getfqdn()), 'port 8443')

server.serve_forever()


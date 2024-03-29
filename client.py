import socket
import pickle
import json
import time

HEADER = 64  # tamanho da primeira msg
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(10)
    client.connect(ADDR)
    client.settimeout(None)
except: print("[CONNECTION ERROR] Connection timeout")

def get():
    back_header = client.recv(HEADER).decode(FORMAT)
    return_message = client.recv(int(back_header)).decode(FORMAT)
    return return_message

def Send_get(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    if msg != DISCONNECT_MESSAGE:
        return get()
        
def Send_post(key, msg):
    structure = {"key":key, "msg":msg}
    message = json.dumps(structure).encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    #print(message, send_lenght)
    client.send(send_lenght)
    client.send(message)
    return get()

Send_get("!GET_TEST")
#Send_post("!POST_TEST", "deree")
Send_get(DISCONNECT_MESSAGE)

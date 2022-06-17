import socket
import threading
import commands
import json

HEADER = 64 #tamanho da primeira msg
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #obtem o IPv4
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handler(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT) #Recebe a primeira msg
        if msg_lenght: #caso exista algum valor na msg
            msg_lenght = int(msg_lenght) #tranforma a mensagem em int para escutar por esse valor dee bytes na próxima msg
            msg = conn.recv(msg_lenght).decode(FORMAT) #espera a mensagem
            
            if DISCONNECT_MESSAGE in msg:
                connected = False
                print(f"[DISCONNECTED] {addr}")
                break
            
            print(f'[{addr}] {msg}')
            if "!GET" in msg:
                return_message = commands.commands[msg]()
                conn.send(return_message[0].encode(FORMAT)) #manda a quantidades de Bytes da próxima msg
                conn.send(return_message[1].encode(FORMAT)) #manda a próxima msg
            
            if "!POST" in msg:
                get_data = json.loads(msg)
                return_message = commands.commands[get_data["key"]](get_data["msg"])
                conn.send(return_message[0].encode(FORMAT)) # manda a quantidades de Bytes da próxima msg
                conn.send(return_message[1].encode(FORMAT))  # manda a próxima msg
        
    conn.close() #fecha a conexão ao sair do loop


def start():
    server.listen() #Faz o serviidor WS começar a escutar novas conecxões
    print(f'[LISTENING] listenng on {SERVER}')
    while True:
        conn, addr = server.accept() #Aceita conexões
        thread = threading.Thread(target=handler, args=(conn, addr)) #Separa as cocxões em Threads para melhorar o desempenho e não criar filas de espera
        thread.start() #Inicia o novo Thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}\n")


if __name__ == "__main__":
    print("[STARTNG] server is starting!")
    start()
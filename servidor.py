'''import socket 
import threading
import time

#O código abaixo busca o IP de forma padrão
SERVER_IP =socket.gethostbyname(socket.gethostname())
#Porta de acesso
PORT = 5050
ADDR = (SERVER_IP,PORT)
FORMATO = 'utf-8'

#Servidor 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conexoes =[]
memsagens =[]

def enviar_mensagem_individual(connection):
    pass
def enviar_mensagem_todos():
    pass
def handle_clientes():
    print("[NOVA CONEXÃO] um novo usuario se conectou pelo endereço {addr}")
    global conexaoes
    nome = False

    while True:
        msg = conn.recv(1024).decode(FORMATO)
def start():
        #Basicamente essa função vai deixar o servidor escutando
        #e quando for chamado ele vai abrir uma threading para a 
        #função handle_clientes sem quebrar o while true da 
        #escuta do servidor
    print("Iniciando socket")
    socket.listen()
    while True:
        conn, addr = socket.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn,addr))
        thread.start()'''

import socket

servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

servidor.bind(('localhost',12000))

while True:
    mensagem_bytes, endereco_ip_cliente = servidor.recvfrom(2048)
    mensagem_resposta = mensagem_bytes.decode().upper()
    servidor.sendto(mensagem_resposta.encode(),endereco_ip_cliente)
    print(mensagem_resposta)
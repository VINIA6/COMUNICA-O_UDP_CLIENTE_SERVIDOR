import socket
import time

#enviar requisição 


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print('Configurações da estufa:')
    print('0 - relatorio')
    print('1 - ligar/desligar Resfriador')
    print('2 - ligar/desligar Aquecedor')
    print('3 - ligar/desligar Irrigador')
    print('4 - ligar/desligar Injetor de Co2')

    Input = int(input('Qual opçao: '))

    if Input==0:
        break #relatorio
    elif Input==1:
        print('1 para ligar \n0 para desligar')
        liga_desliga = str(5050)
        cliente.sendto(liga_desliga.encode(),("localhost",12000))
        lig_desl, endereco_ip_servidor =  cliente.recvfrom(2048)


'''
while True:
    mensagem_envio = input('Digite a mensagem:' )
    cliente.sendto(mensagem_envio.encode(),("localhost",12000))
    mensagem_bytes, endereco_ip_servidor =  cliente.recvfrom(2048)
    print(endereco_ip_servidor)
    print(mensagem_bytes.decode())
cont = 0 
while True:
    temp = str(sensor.tempertura(cont,38.1))
    cliente.sendto(temp.encode(),("localhost",12000))
    mensagem_bytes1, endereco_ip_servidor =  cliente.recvfrom(2048)

    co2 = str(sensor.co2(cont,10))
    cliente.sendto(co2.encode(),("localhost",12000))
    mensagem_bytes2, endereco_ip_servidor =  cliente.recvfrom(2048)

    humidade = str(sensor.humidade(cont,50))
    cliente.sendto(humidade.encode(),("localhost",12000))
    mensagem_bytes3, endereco_ip_servidor =  cliente.recvfrom(2048)

    cont = cont+1
    time.sleep(1)
'''
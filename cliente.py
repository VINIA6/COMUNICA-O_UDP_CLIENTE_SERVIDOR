import socket
import sensores
import time
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

'''while True:
    mensagem_envio = input('Digite a mensagem:' )
    cliente.sendto(mensagem_envio.encode(),("localhost",12000))
    mensagem_bytes, endereco_ip_servidor =  cliente.recvfrom(2048)
    print(endereco_ip_servidor)
    print(mensagem_bytes.decode())'''
cont = 0 
while True:
    temp = str(sensores.sensor_tempertura(cont))
    cliente.sendto(temp.encode(),("localhost",12000))
    mensagem_bytes1, endereco_ip_servidor =  cliente.recvfrom(2048)

    co2 = str(sensores.nivel_co2(cont))
    cliente.sendto(co2.encode(),("localhost",12000))
    mensagem_bytes2, endereco_ip_servidor =  cliente.recvfrom(2048)

    humidade = str(sensores.nivel_co2(cont))
    cliente.sendto(humidade.encode(),("localhost",12000))
    mensagem_bytes3, endereco_ip_servidor =  cliente.recvfrom(2048)

    cont = cont+1
    time.sleep(1)
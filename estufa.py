from sensores import sensor
from sensores import atuador
import socket
import time

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cont = 0 

temp = str(sensor.tempertura(38.1))
while True:
    
    cliente.sendto(temp.encode(),("localhost",12000))
    mensagem_bytes1, endereco_ip_servidor =  cliente.recvfrom(2048)
    mensagem_bytes1 =  mensagem_bytes1.decode()
    temp = str(mensagem_bytes1)
    ''' temp = mensagem_bytes1
    temp = temp.decode()'''

    '''co2 = str(sensor.co2(cont,10))
    cliente.sendto(co2.encode(),("localhost",12000))
    mensagem_bytes2, endereco_ip_servidor =  cliente.recvfrom(2048)

    humidade = str(sensor.humidade(cont,50))
    cliente.sendto(humidade.encode(),("localhost",12000))
    mensagem_bytes3, endereco_ip_servidor =  cliente.recvfrom(2048)'''
    '''temp = float(temp)
    print(temp)'''
    
    time.sleep(1)
    
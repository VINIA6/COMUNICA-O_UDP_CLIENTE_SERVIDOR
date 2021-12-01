import socket
from sensores import atuador

servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind(('localhost',12000))

# montar dicionario com liga desliga, dependendo da requisição do verifique os if e else dentro do while true  
novo = 0
atual = 0
while True:
      
        mensagem_bytes1, endereco_ip_cliente1 = servidor.recvfrom(2048)
        mensagem_bytes1_real = float(mensagem_bytes1)
        
        x=novo
        novo = mensagem_bytes1_real
        antigo = x 

        if mensagem_bytes1_real == 5050.0 :
                temperatura =  atuador.Resfriador(antigo)
                print('ATUADOR: ',temperatura)
                mensagem_resposta1 = str(temperatura)
                servidor.sendto(mensagem_resposta1.encode(),endereco_ip_cliente1)
        '''else:
                mensagem_resposta1 = mensagem_bytes1.decode()
                servidor.sendto(mensagem_resposta1.encode(),endereco_ip_cliente1)'''

        '''lig_desl, endereco_ip_cliente2 = servidor.recvfrom(2048)'''
        '''def exec():
                async_call = pool.apply_async(cond_cliente)
                return async_call
       

        print(exec())'''
        
        '''
        
        
                        mensagem_resposta1 = float(mensagem_resposta1)
                        mensagem_resposta1 = mensagem_resposta1 + 10.0
                        mensagem_resposta1 = str(mensagem_resposta1)
                        
                        mensagem_bytes1 = atuador.Aquecedor(float(mensagem_bytes1))
                        mensagem_bytes1 = exec()'''
        
        '''mensagem_bytes2, endereco_ip_cliente = servidor.recvfrom(2048)
        mensagem_resposta2 = mensagem_bytes1.decode()
        servidor.sendto(mensagem_resposta2.encode(),endereco_ip_cliente)

        mensagem_bytes3, endereco_ip_cliente = servidor.recvfrom(2048)
        mensagem_resposta3 = mensagem_bytes1.decode()
        servidor.sendto(mensagem_resposta3.encode(),endereco_ip_cliente)'''

        '''
        print('CO2:',float(mensagem_bytes2))
        print('Humidade', float(mensagem_bytes3) )
        print('Temperatura', float(mensagem_bytes1))
        '''
        print('Temperatura', float(mensagem_bytes1))
    





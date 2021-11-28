import socket


servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

servidor.bind(('localhost',12000))

while True:
    mensagem_bytes1, endereco_ip_cliente = servidor.recvfrom(2048)
    mensagem_resposta1 = mensagem_bytes1.decode()
    servidor.sendto(mensagem_resposta1.encode(),endereco_ip_cliente)

    mensagem_bytes2, endereco_ip_cliente = servidor.recvfrom(2048)
    mensagem_resposta2 = mensagem_bytes1.decode()
    servidor.sendto(mensagem_resposta2.encode(),endereco_ip_cliente)

    mensagem_bytes3, endereco_ip_cliente = servidor.recvfrom(2048)
    mensagem_resposta3 = mensagem_bytes1.decode()
    servidor.sendto(mensagem_resposta3.encode(),endereco_ip_cliente)

    print('CO2:',mensagem_bytes2 ,'%')
    print('Temperatura', mensagem_bytes1)
    print('Humidade', mensagem_bytes3 )

    if float(mensagem_bytes1) > 42 :
        print('Stop sensores -> TEMPERATURA')
        break
    if float(mensagem_bytes3) > 65:
        print('Stop sensores -> HUMIDADE')
        break
    if float(mensagem_bytes3) > 70:
        print('Stop sensores -> CO2')
        break


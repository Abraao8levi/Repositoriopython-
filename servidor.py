import socket

HOST = '127.0.0.1'  # endereço IP do servidor
PORT = 8080        # porta usada pelo servidor

# cria um objeto de soquete
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # vincula o soquete ao endereço IP e à porta
    s.listen()  # aguarda conexões de clientes
    conn, addr = s.accept()  # aceita uma conexão de cliente
    with conn:
        print('Conectado por', addr)
        while True:
   data = conn.recv(1024)  # recebe dados do cliente
        if not data:
           break
 conn.sendall(data)  # envia os dados de volta para o cliente

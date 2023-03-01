import socket

HOST = '127.0.0.1'  # endereço IP do servidor
PORT = 8080        # porta usada pelo servidor

# cria um objeto de soquete
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # conecta-se ao servidor
    s.sendall(b'Ola, servidor!')  # envia dados ao servidor
    data = s.recv(1024)  # recebe dados do servidor
    print('Mensagem recebida:', data.decode())  # exibe a mensagem recebida

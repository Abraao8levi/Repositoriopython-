import socket

# define o endereço IP e porta do servidor
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# cria um objeto socket do tipo UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# vincula o soquete ao endereço IP e porta do servidor
sock.bind((UDP_IP, UDP_PORT))

# aguarda a chegada de dados
while True:
  data, addr = sock.recvfrom(1024)  # recebe os dados e endereço do cliente
  print("Mensagem recebida:", data.decode())
  sock.sendto("Mensagem recebida com sucesso!".encode(), addr)  # envia uma resposta para o cliente

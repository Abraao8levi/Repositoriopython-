import socket

# define o endereço IP e porta do servidor
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# cria um objeto socket do tipo UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia uma mensagem para o servidor
mensagem = "Ola, servidor!"
sock.sendto(mensagem.encode(), (UDP_IP, UDP_PORT))

# aguarda a resposta do servidor
data, addr = sock.recvfrom(1024)
print("Resposta do servidor:", data.decode())

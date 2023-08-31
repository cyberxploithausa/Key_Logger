import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 5555
c.connect((host, port))

sako = c.recv(1024)
print(sako.decode("utf-8"))
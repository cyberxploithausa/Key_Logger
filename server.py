import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5555

s.bind((host, port))
s.listen(5)

run = True

while run:
	cliSoc, addr = s.accept()
	print(f"{addr} Yayi connecting da a yanzu!")
	cliSoc.send(bytes("Barka da zuwa wannan server din cyberXploit", "utf-8"))
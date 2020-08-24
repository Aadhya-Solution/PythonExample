import socket

s = socket.socket()
host = socket.gethostname()
port = 12349

s.connect((host, port))

input_string = raw_input("Enter data you want to send->")
s.sendall(input_string)

print s.recv(1024)

s.close()

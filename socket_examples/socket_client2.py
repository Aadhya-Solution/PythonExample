# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data=raw_input("What u want to send:")
    s.send(data)
    senddata = s.recv(1024)
    print 'Received', str(senddata)
s.close()
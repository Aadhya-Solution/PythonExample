# Echo server program
import socket
# class Prime:
#     def __int__(self):
#         pass
#     def prime(self,num):
#         flag=True
#         for i in range(2,num):
#             if num%i==0:
#                 flag=False
#         return flag

def get_prinme(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag
# c=Prime()

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(4000)
    #if not data: break
    print "Got:",data
    a=eval(data)
    if get_prinme(a):
        data="%d Its Prime Number"%(a)
    else:
        data="%d Its not Prime Number"%(a)
    conn.send(data)
conn.close()
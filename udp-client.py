import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto('I am Saeid Attar'.encode(),('localhost',14200))

data=s.recv(123456)
print(data.decode())
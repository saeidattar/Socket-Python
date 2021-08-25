from os import pardir
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',14200))
print("server on port 14200is active")

while True:
    connection,client=s.recvfrom(123456)
    print("Recieved from"+str(connection.decode()))
    data=time.ctime()
    s.sendto(data.encode(),client)
connection.close()
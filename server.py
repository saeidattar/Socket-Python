import socket
import time
from colorama import Fore


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",14200))
s.listen(1)
print("server On port 14200 is active!!!!!!!!  ")

while True:    
    connection,client=s.accept()
    print(connection,"is accept")
    print("Client",client,"connected")

    data=connection.recv(4096)
    print("Recieved",data.decode())
    data=time.ctime()
    connection.send(str.encode(data))
    connection.close()

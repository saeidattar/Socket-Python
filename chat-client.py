import socket
from colorama import Fore

s=socket.socket(2,1)
 
name=input(Fore.GREEN+"what is your name? :")
ip=input(Fore.WHITE+"what is your ip? :")
port=input(Fore.BLUE+"what is your port? :")

s.connect((ip,int(port)))

print(Fore.CYAN+'connected !!!!!!!!')

while True:
    data=s.recv(123456)
    print(data.decode())

    pm=input(Fore.BLUE+">>>>>>>:")
    data=name+' : '+pm
    s.send(data.encode())
s.close()
    
    
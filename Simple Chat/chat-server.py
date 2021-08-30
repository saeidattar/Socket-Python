import socket
from colorama import Fore

s=socket.socket(2,1)
 
name=input(Fore.GREEN+"what is your name? :")
ip=input(Fore.WHITE+"what is your ip? :")
port=input(Fore.BLUE+"what is your port? :")

s.bind((ip,int(port)))
s.listen(5)

print(Fore.RED+"Server On Port "+str(port))

connection,client=s.accept()
print(Fore.GREEN+"Connected to >>>>>>> :"+str(client))

while True:
    pm=input(Fore.BLUE+">>>>>>>:")
    data=name+' : '+pm
    connection.send(data.encode())
    sms=connection.recv(123456)
    print(sms.decode())
connection.close()

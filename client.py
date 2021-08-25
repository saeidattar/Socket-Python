import socket

connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect(("localhost",14200))
print("connected to server")
message="Hello I am Saeid Attar"
connection.send(message.encode())
data=connection.recv(100)
print(data.decode())
connection.close()
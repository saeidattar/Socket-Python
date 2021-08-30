import socket


connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

connection.connect(("172.217.18.132",80))
print("connected!!!")
connection.send("GET /text.txt /HTTP/1.1\n\n".encode())
data=connection.recv(1000)
print(data.decode())
connection.close()
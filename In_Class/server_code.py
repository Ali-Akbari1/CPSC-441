import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind("127.0.0.1", 12345)
server_socket.listen(1) 
print("server is waiting for connection...")

conn.settimeout(10)
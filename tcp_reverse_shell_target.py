import socket                

s = socket.socket()          

host = "localhost"
port = 2468                

try:
    s.connect((host, port)) 

    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))

    s.close() 
except socket.error as msg:
    print("[The server is not active..] message:", msg)

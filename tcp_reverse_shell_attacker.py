import socket

host = "localhost"
port = 2468

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port)) 
    print("socket {} connected to the port".format(port))

    s.listen(1)      
    print("listening")
except socket.error as msg:
    print("error:",msg)

while True: 

   c, addr = s.accept()      
   print('connection', addr)

   message = 'connected'
   c.send(message.encode('utf-8')) 

   c.close()

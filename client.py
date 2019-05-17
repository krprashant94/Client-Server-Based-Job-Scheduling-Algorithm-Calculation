import socket 

s = socket.socket() 

port = 12345

s.connect(('127.0.0.1', port)) 
print (str(s.recv(1024).decode()))
s.close() 
input()

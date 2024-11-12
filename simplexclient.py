#importing modules
import socket
import sys
import time

#Create socket and accept user input hostname
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
server_port = 8080

#Connecting to the server
print("This is your IP address: ", ip)
server_host = input("Enter your friend's IP: ") #Need exact IP address
name = input("Enter your nickname: ")

socket_server.connect((server_host,server_port)) #Host name of server and the port are bounded together and also connected to socket

#Retrieving the message
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined.")

while True: 
    message = socket_server.recv(1024).decode() #To receive message, socket invokes the recv() to accept 1024 bytes of data.
    #This data is stored in the message object and decoded using the decoded.
    print(server_name, ": ", message) #The message is then printed with the hostname of the server and message is received
    message = input("Me: ")
    socket_server.send(message.encode())
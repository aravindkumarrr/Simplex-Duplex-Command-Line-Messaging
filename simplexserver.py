
#importing the necessary modules
import socket #Contains necessary functions to use sockets.
import sys #Provides data related to system.
import time #Time-related descriptions and conversion operations.

#Creating hostnames and retrieving hostnames
new_socket = socket.socket() #Socket() is a constructor for the socket library
host_name = socket.gethostname() #Once socket is created, we retrieve local host name device
s_ip = socket.gethostbyname(host_name) #gets ip address of the other user when host_name is passed

port = 8080 #Specifically this port because this is most default port that most machines use

#Now we bind host and port
new_socket.bind((host_name, port))
print("Binding Successful...")
print("Your ip is: ", s_ip)

#Listen for connections
name = input("Enter your nickname: ")
new_socket.listen(1) #listen() takes one argument, which is the number of connections.

#Accepting incomming connections
conn, address = new_socket.accept() #First variable conn is connected to socket; Second variable address is assigned to ip address of client
print("Received Connection from ", address[0])
print("Connection Established. Connected from ", address[0])

#Storing incoming connection data
#Used the details of the incoming connection and stored them in variable called client.
client = (conn.recv(1024)).decode() #Variable client can be a maximum of 1024 bytes
print(client + " has connected.")
conn.send(name.encode())

#Delivering messages
while True:
    message = input("Me: ") #User enters the message
    conn.send(message.encode()) #The message is encoded. The message is sent through the send(), invoked on the connection object
    message = conn.recv(1024) #Incoming message is received from the conn object, which can maximum receive 1024 bytes of information.
    message = message.decode() #The message is decoded on the server side using decode()
    print(client,": ", message)

#This is the end of the server side
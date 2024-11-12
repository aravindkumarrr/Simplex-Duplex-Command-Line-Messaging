import socket
import threading


def send_messages(socket_server,name):
    # Function to send messages to the server
    while True:
        message = input()
        tempf= f"{name}: "+ message
        socket_server.send(tempf.encode())  # Encode and send the message

def receive_messages(socket_server, server_name):
    # Function to receive messages from the server
    while True:
        try:
            message = socket_server.recv(1024).decode()  # Receive and decode the message
            if message:
                print(f"{message}")
            else:
                # Handle disconnection
                print("Server has disconnected.")
                break
        except:
            # Handle any connection errors
            print("Connection error.")
            break

def main():
    # Creating socket and getting server information
    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    server_port = 8080

    # Display IP and get friend's IP and nickname
    print("This is your IP address:", ip)
    server_host = input("Enter IP: ")
    name = input("Enter your nickname: ")

    # Connecting to the server
    socket_server.connect((server_host, server_port))
    socket_server.send(name.encode())  # Send nickname to server

    # Receiving server's nickname
    server_name = socket_server.recv(1024).decode()
    print(f"{server_name} has joined the chat.")

    # Start send and receive threads
    receive_thread = threading.Thread(target=receive_messages, args=(socket_server, server_name))
    send_thread = threading.Thread(target=send_messages, args=(socket_server,name))


    send_thread.start()
    receive_thread.start()

    # Wait for threads to complete (they run indefinitely until closed)
    send_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()
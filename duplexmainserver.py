import socket
import threading

def send_messages(conn,name):
    # Function to send messages to the client
    while True:
        message=input()
        temp=f"{name}: "+ message
        conn.send(temp.encode())  # Encode and send the message

def receive_messages(conn, client_name):
    # Function to receive messages from the client
    while True:
        try:
            message = conn.recv(1024).decode()  # Receive and decode the message
            if message:
                print(message)
            else:
                # Handle disconnection
                print("Client has disconnected.")
                break
        except:
            # Handle any connection errors
            print(message)
            break

def main():
    # Creating socket and getting host info
    new_socket = socket.socket()
    host_name = socket.gethostname()
    s_ip = socket.gethostbyname(host_name)

    port = 8080
    new_socket.bind((host_name, port))
    print("Binding Successful...")
    print("Your IP is:", s_ip)

    # Listening for incoming connections
    name = input("Enter your nickname: ")
    new_socket.listen(1)
    print("Waiting for incoming connections...")

    # Accepting the incoming connection
    conn, address = new_socket.accept()
    print("Connection Established. Connected from:", address[0])

    # Receiving client's nickname
    client_name = conn.recv(1024).decode()
    print(f"{client_name} has connected.")
    conn.send(name.encode())  # Send your nickname to the client

    # Starting send and receive threads
    send_thread = threading.Thread(target=send_messages, args=(conn,name))
    receive_thread = threading.Thread(target=receive_messages, args=(conn,name))

    send_thread.start()
    receive_thread.start()

    # Wait for threads to complete (they run indefinitely until closed)
    send_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()

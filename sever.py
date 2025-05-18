import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()
print("Server is listening on port 9999...")

client, addr = server.accept()
print(f"Connection from {addr} has been established.")
done = False

while not done:
    try:
        msg = client.recv(1024).decode('utf-8')
        if msg.lower() == 'quit':
            print("Client ended the chat.")
            done = True
        else:
            print(f"Client: {msg}")
            response = input("Server: ")
            client.send(response.encode('utf-8'))

            if response.lower() == 'quit':
                print("You ended the chat.")
                done = True
    except ConnectionResetError:
        print("Client disconnected unexpectedly.")
        done = True
    except ConnectionAbortedError:
        print("Connection aborted.")
        done = True

client.close()
server.close()

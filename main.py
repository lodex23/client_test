import socket
import json
import threading

def receive_messages(client_socket):
    while True:
        # Receiving messages from the server
        response = client_socket.recv(1024).decode()
        json_data = json.loads(response)

        message = json_data.get("message", "No message")
        print(f"{message}")

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Getting user input for the username
    username = input("Enter your username: ")

    # Sending the username to the server
    client_socket.send(username.encode())

    # Start a separate thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Getting user input for the message
        message = input()

        if message.lower() == 'exit':
            break

        # Creating a JSON payload
        json_data = {"message": message}
        json_payload = json.dumps(json_data)

        # Sending the JSON payload to the server
        client_socket.send(json_payload.encode())

    # Closing the client socket
    client_socket.close()

if __name__ == "__main__":
    start_client()

import socket
import threading

HOST = '0.0.0.0'  # Bind to all interfaces (required for public exposure)
PORT = 5000       # Must match what you expose on Northflank

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            broadcast(message, client_socket)
        except:
            break

    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server running on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    start_server()

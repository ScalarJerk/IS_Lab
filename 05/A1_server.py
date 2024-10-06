import socket
import hashlib


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print('Server is waiting for connections...')

    num_connections = 0
    while True:
        connection, client_address = server_socket.accept()
        print('Connection from', client_address)
        num_connections += 1
        print(f"Number of connections: {num_connections}")

        try:
            data = connection.recv(1024)
            if data == b'exit' or not data or num_connections == 3:
                break

            # Compute hash of the received data
            data_hash = hashlib.sha256(data).hexdigest()

            # Send hash back to client
            connection.sendall(data_hash.encode())

        finally:
            connection.close()

    server_socket.close()
    print("Server shutting down.")


if __name__ == "__main__":
    start_server()
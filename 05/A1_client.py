import socket
import hashlib


def send_message():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)

    try:
        client_socket.connect(server_address)

        data_to_send = input("Enter data (or 'exit' to quit): ").encode()

        if data_to_send == b'exit' or not data_to_send:
            print("Exiting...")
            return

        client_socket.sendall(data_to_send)

        # Compute local hash
        local_hash = hashlib.sha256(data_to_send).hexdigest()

        # Receive hash from server
        received_hash = client_socket.recv(64).decode()

        print(f'Received hash: {received_hash}')
        print(f'Local hash: {local_hash}')

        if received_hash == local_hash:
            print('Data integrity verified: Hashes match.')
        else:
            print('Data integrity failed: Hashes do not match.')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client_socket.close()


if __name__ == "__main__":
    send_message()
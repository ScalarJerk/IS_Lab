'''
Using socket programming in Python, demonstrate the application of
hash functions for ensuring data integrity during transmission over a
network. Write server and client scripts where the server computes the
hash of received data and sends it back to the client, which then verifies
the integrity of the data by comparing the received hash with the locally
computed hash. Show how the hash verification detects data corruption
or tampering during transmission.
'''

import socket
import hashlib

data_to_send = input("Enter data:- ").encode()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
client_socket.connect(server_address)
try:
    if data_to_send == b'exit' or not data_to_send:
        exit()
    client_socket.sendall(data_to_send)
    received_hash = client_socket.recv(64).decode()
    local_hash = hashlib.sha256(data_to_send).hexdigest()
    print(f'Received hash: {received_hash}')
    print(f'Local hash: {local_hash}')
    if received_hash == local_hash:
        print('Data integrity verified: Hashes match.')
    else:
        print('Data integrity failed: Hashes do not match.')
except Exception as e:
    print("Exception occured", e)
finally:
    client_socket.close()
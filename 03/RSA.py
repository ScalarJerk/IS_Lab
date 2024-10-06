# Import necessary modules from pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# This module converts binary data to hexadecimal
from binascii import hexlify


# Step2: Generate new RSA key
# Create an RSA key pair with a key size of 1024 bits
key = RSA.generate(1024)

# Set the private_key variable to the generated key
private_key = key

# Derive the public key from the generated key
public_key = key.publickey()


# Step3: Encrypt using public key
# Create a PKCS1_OAEP cipher object with the public key for encryption
data_to_encrypt = b"Hello, this is a message to be encrypted."
cipher_rsa = PKCS1_OAEP.new(public_key)

# Encrypt the provided data using the public key
encrypted = cipher_rsa.encrypt(data_to_encrypt)

# Convert binary data to hexadecimal for display using hexlify
print("Encrypted:", hexlify(encrypted))


# Step4: Decrypt using private key
# Create a PKCS1_OAEP cipher object with the private key for decryption
cipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa.decrypt(encrypted)

# Display the decrypted result as a UTF-8 encoded string
print("Decrypted:", decrypted.decode("utf-8"))
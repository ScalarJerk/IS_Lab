from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import HKDF

# 1. Generate ECC key pairs
private_key = ECC.generate(curve='P-256') # another curve used in question 4 is secp256r1
public_key = private_key.public_key()

# Serialize public key to PEM format (for demonstration)
pem_public_key = public_key.export_key(format='PEM')

# Display generated keys (for demonstration purposes)
print("Public Key (PEM):")
print(pem_public_key)

# 2. Simulate key exchange and derive shared secret
# Generate another key pair for demonstration (for other party)
other_private_key = ECC.generate(curve='P-256')
other_public_key = other_private_key.public_key()

# Derive shared point
shared_point = private_key.d * other_public_key.pointQ

# Convert shared point to bytes
shared_secret = shared_point.x.to_bytes(32, 'big') + shared_point.y.to_bytes(32, 'big')

# Derive AES key from shared secret using HKDF
aes_key = HKDF(shared_secret, 32, salt=b'', context=b'aes_key', hashmod=SHA256)

# Example message to encrypt
message = b"Secure Transactions"

# 3. Encrypt data with AES-GCM
# Generate a random nonce
nonce = get_random_bytes(12)
cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
ciphertext, tag = cipher.encrypt_and_digest(message)

print("Ciphertext:", ciphertext.hex())
print("Nonce:", nonce.hex())
print("Tag:", tag.hex())

# 4. Decrypt data with AES-GCM
cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)

print("Decrypted message:", decrypted_message.decode())
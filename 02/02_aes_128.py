import os
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

# To encrypt a block of plaintext, we need to provide an Initialization Vector and a Key
# return Key
def getKey(keysize):

    key = os.urandom(keysize)
    return key
# return Initialization Vector
def getIV(blocksize):

    iv = os.urandom(blocksize)
    return iv

KEYSIZE = 16

BLOCKSIZE = 16

plaintext1 = "Hello! Welcome to The Security Buddy !! "

key = getKey(KEYSIZE)
iv = getIV(BLOCKSIZE)

cipher1=AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher1.encrypt(pad(plaintext1.encode(), BLOCKSIZE))
print(ciphertext)

cipher2 =AES.new(key, AES.MODE_CBC, iv)
plaintext2 =unpad(cipher2.decrypt(ciphertext), BLOCKSIZE)
print(plaintext2.decode())

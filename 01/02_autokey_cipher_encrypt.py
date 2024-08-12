# A Python program to illustrate
# Autokey Cipher Technique

# Importing required library
import re

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    msg = "HELLO"
    key = "N"
    #msg = input("Enter plaintext\t")
    #key = int(input("Enter shift value\t"))

    # Check if key is a number and convert it to a character if necessary
    if re.match(r"[-+]?(\d*\.\d+|\d+)", key):
        key = alphabet[int(float(key)) % 26]
        
    enc = auto_encryption(msg, key)

    print("Plaintext : " + msg)
    print("Encrypted : " + enc)
    print("Decrypted : " + auto_decryption(enc, key))

def auto_encryption(msg, key):
    len_msg = len(msg)

    # Generating the keystream
    new_key = key + msg
    new_key = new_key[:len_msg]
    encrypt_msg = ""

    # Applying encryption algorithm
    for x in range(len_msg):
        first = alphabet.index(msg[x])
        second = alphabet.index(new_key[x])
        total = (first + second) % 26
        encrypt_msg += alphabet[total]
    
    return encrypt_msg

def auto_decryption(msg, key):
    current_key = key
    decrypt_msg = ""

    # Applying decryption algorithm
    for x in range(len(msg)):
        get1 = alphabet.index(msg[x])
        get2 = alphabet.index(current_key[x])
        total = (get1 - get2) % 26
        total = total if total >= 0 else total + 26
        decrypt_msg += alphabet[total]
        current_key += alphabet[total]
    
    return decrypt_msg

if __name__ == "__main__":
    main()

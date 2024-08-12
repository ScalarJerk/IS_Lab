def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            # Convert to uppercase to have a consistent range
            char = char.upper()
            # Apply the multiplicative cipher formula
            encrypted_char = chr(((ord(char) - ord('A')) * key) % 26 + ord('A'))
            cipher_text += encrypted_char
        else:
            # If the character is not a letter, leave it unchanged
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    # Calculate the modular multiplicative inverse of the key
    key_inverse = pow(key, -1, 26)
    for char in cipher_text:
        if char.isalpha():
            char = char.upper()
            # Apply the multiplicative cipher decryption formula
            decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) % 26 + ord('A'))
            plain_text += decrypted_char
        else:
            plain_text += char
    return plain_text

# Example
plain_text = input("Enter plaintext\t")
key = int(input("Enter shift value\t"))

# Encryption
cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text)

# Decryption
decrypted_text = decrypt(cipher_text, key)
print("Decrypted:", decrypted_text)

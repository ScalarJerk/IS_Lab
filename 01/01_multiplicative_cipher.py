def multiplicative_cipher(text, key, mode='encrypt'):
    result = ""
    for char in text.upper():
        if char.isalpha():
            if mode == 'encrypt':
                result += chr(((ord(char) - 65) * key) % 26 + 65)
            else:
                for i in range(26):
                    if (i * key) % 26 == (ord(char) - 65):
                        result += chr(i + 65)
                        break
        else:
            result += char
    return result

# b) Multiplicative cipher with key = 15
multiplicative_encrypted = multiplicative_cipher("message", 15, 'encrypt')
multiplicative_decrypted = multiplicative_cipher(multiplicative_encrypted, 15, 'decrypt')

print("\nMultiplicative Cipher:")
print(f"Encrypted: {multiplicative_encrypted}")
print(f"Decrypted: {multiplicative_decrypted}")
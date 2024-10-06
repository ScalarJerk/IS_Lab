def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.upper()
    text = text.upper()
    key_length = len(key)
    key_as_int = [ord(i) for i in key]

    for i, char in enumerate(text):
        if char.isalpha():
            if mode == 'encrypt':
                result += chr((ord(char) + key_as_int[i % key_length] - 2 * 65) % 26 + 65)
            else:
                result += chr((ord(char) - key_as_int[i % key_length] + 26) % 26 + 65)
        else:
            result += char
    return result
# 1. Vigenere cipher
message1 = "THEHOUSEISBEINGSOLDTONIGHT"
key1 = "DOLLARS"

vigenere_encrypted = vigenere_cipher(message1, key1, 'encrypt')
vigenere_decrypted = vigenere_cipher(vigenere_encrypted, key1, 'decrypt')

print("Vigenere Cipher:")
print(f"Encrypted: {vigenere_encrypted}")
print(f"Decrypted: {vigenere_decrypted}")

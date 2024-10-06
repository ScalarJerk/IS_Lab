# Implementation of Affine Cipher in Python

def affine_cipher(text, a, b, mode='encrypt'):
    result = ""
    for char in text.upper():
        if char.isalpha():
            if mode == 'encrypt':
                result += chr(((ord(char) - 65) * a + b) % 26 + 65)
            else:
                for i in range(26):
                    if (i * a) % 26 == (ord(char) - 65 - b) % 26:
                        result += chr(i + 65)
                        break
        else:
            result += char
    return result

# c) Affine cipher with key = (15, 20)
affine_encrypted = affine_cipher("Hello I like oranges", 15, 20, 'encrypt')
affine_decrypted = affine_cipher(affine_encrypted, 15, 20, 'decrypt')

print("\nAffine Cipher:")
print(f"Encrypted: {affine_encrypted}")
print(f"Decrypted: {affine_decrypted}")
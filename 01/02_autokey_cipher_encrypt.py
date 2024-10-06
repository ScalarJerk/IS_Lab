def autokey_cipher(text, key, mode='encrypt'):
    result = ""
    text = text.upper()

    if mode == 'encrypt':
        full_key = [key] + [ord(char) - 65 for char in text[:-1]]
    else:
        full_key = [key]

    for i, char in enumerate(text):
        if char.isalpha():
            if mode == 'encrypt':
                shift = full_key[i]
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                shift = full_key[i]
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
                result += decrypted_char
                full_key.append(ord(decrypted_char) - 65)
        else:
            result += char
    return result

# 2. Autokey cipher
message2 = "THEHOUSEISBEINGSOLDTONIGHT"
key2 = 7

autokey_encrypted = autokey_cipher(message2, key2, 'encrypt')
autokey_decrypted = autokey_cipher(autokey_encrypted, key2, 'decrypt')

print("\nAutokey Cipher:")
print(f"Original: {message2}")
print(f"Encrypted: {autokey_encrypted}")
print(f"Decrypted: {autokey_decrypted}")
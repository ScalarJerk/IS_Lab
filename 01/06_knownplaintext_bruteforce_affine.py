def modular_inverse(a, m):
    # Function to find the modular inverse of a mod m using Extended Euclidean Algorithm
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""
    a_inv = modular_inverse(a, 26)  # Find the modular inverse of a mod 26
    if a_inv is None:
        return None  # If there's no modular inverse, skip this key
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - 65  # Convert to 0-25 range
            x = (a_inv * (y - b)) % 26  # Apply decryption formula
            decrypted_text += chr(x + 65)  # Convert back to character
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_affine(ciphertext, known_plaintext, encrypted_pair):
    for a in range(1, 26):
        if modular_inverse(a, 26) is not None:  # Only consider valid values for a
            for b in range(26):
                decrypted = affine_decrypt(encrypted_pair, a, b)
                if decrypted == known_plaintext.upper():  # Check if decrypted matches known plaintext
                    print(f"Found key: a = {a}, b = {b}")
                    print(f"Decrypted message: {affine_decrypt(ciphertext, a, b)}")
                    return

# Given ciphertext and known plaintext/encrypted pair
ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"
known_plaintext = "AB"
encrypted_pair = "GL"

# Brute-force search for the key and decryption
brute_force_affine(ciphertext, known_plaintext, encrypted_pair)

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Calculate the shifted character
            shifted = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext += shifted
        else:
            plaintext += char  # Non-alphabet characters are unchanged
    return plaintext

def determine_shift(ciphertext, known_plaintext):
    # Assume all characters are uppercase, calculate shift using the first character
    shift = (ord(ciphertext[0]) - ord(known_plaintext[0])) % 26
    return shift

# Given ciphertext and known plaintext
ciphertext = "CIW"
known_plaintext = "YES"

# Determine the shift based on the known plaintext attack
shift = determine_shift(ciphertext, known_plaintext)
print(f"Detected shift: {shift}")

# Decrypt the longer ciphertext using the found shift
longer_ciphertext = "XVIEWYWI"
decrypted_message = caesar_decrypt(longer_ciphertext, shift)

print(f"Decrypted message: {decrypted_message}")

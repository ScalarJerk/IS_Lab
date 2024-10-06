def create_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)


def playfair_cipher(text, key, mode='encrypt'):
    matrix = create_playfair_matrix(key)
    text = text.upper().replace("J", "I")
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        row1, col1 = find_position(matrix, text[i])
        row2, col2 = find_position(matrix, text[i + 1])

        if row1 == row2:
            if mode == 'encrypt':
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == 'encrypt':
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    return result

# 3. Playfair cipher
message3 = "THEKEYISHIDDENUNDERTHEDOORPAD"
key3 = "GUIDANCE"

playfair_encrypted = playfair_cipher(message3, key3, 'encrypt')
playfair_decrypted = playfair_cipher(playfair_encrypted, key3, 'decrypt')

print("\nPlayfair Cipher:")
print(f"Encrypted: {playfair_encrypted}")
print(f"Decrypted: {playfair_decrypted}")

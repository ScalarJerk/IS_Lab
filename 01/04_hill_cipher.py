def matrix_multiply(a, b):
    # Matrix multiplication function for 2x2 matrix and 2x1 vector
    return [
        (a[0][0] * b[0] + a[0][1] * b[1]) % 26,
        (a[1][0] * b[0] + a[1][1] * b[1]) % 26
    ]


def determinant_2x2(matrix):
    # Calculate the determinant of a 2x2 matrix
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26


def matrix_inverse_2x2(matrix):
    # Calculate the inverse of a 2x2 matrix mod 26
    det = determinant_2x2(matrix)
    det_inv = pow(det, -1, 26)  # Modular multiplicative inverse of the determinant

    # Adjugate matrix for 2x2
    adj_matrix = [[matrix[1][1], -matrix[0][1]],
                  [-matrix[1][0], matrix[0][0]]]

    # Apply modular inverse to adjugate matrix
    inv_matrix = [
        [(det_inv * adj_matrix[0][0]) % 26, (det_inv * adj_matrix[0][1]) % 26],
        [(det_inv * adj_matrix[1][0]) % 26, (det_inv * adj_matrix[1][1]) % 26]
    ]

    return inv_matrix


def hill_cipher(text, key, mode='encrypt'):
    text = text.upper().replace(" ", "")
    key_matrix = [key[:2], key[2:]]  # Reshaping the flat key list into 2x2 matrix

    # Pad the text if necessary
    if len(text) % 2 != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), 2):
        pair = [ord(text[i]) - 65, ord(text[i + 1]) - 65]  # Convert letters to numbers (A=0, B=1, etc.)

        if mode == 'encrypt':
            encrypted_pair = matrix_multiply(key_matrix, pair)
        else:
            inv_matrix = matrix_inverse_2x2(key_matrix)
            encrypted_pair = matrix_multiply(inv_matrix, pair)

        result += chr(int(encrypted_pair[0]) + 65) + chr(int(encrypted_pair[1]) + 65)  # Convert numbers back to letters

    return result


# 4. Hill cipher
message4 = "Thequickbrownfoxjumpsoverthelazydogwhileitseeksoutthehiddenpathwaythroughtherainforest"
key4 = [3, 3, 2, 7]

hill_encrypted = hill_cipher(message4, key4, 'encrypt')
hill_decrypted = hill_cipher(hill_encrypted, key4, 'decrypt')

print("\nHill Cipher:")
print(f"Encrypted: {hill_encrypted}")
print(f"Decrypted: {hill_decrypted}")
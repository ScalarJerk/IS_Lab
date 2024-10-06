'''
Implement the hash function in Python. Your function should start with
an initial hash value of 5381 and for each character in the input string,
multiply the current hash value by 33, add the ASCII value of the
character, and use bitwise operations to ensure thorough mixing of the
bits. Finally, ensure the hash value is kept within a 32-bit range by
applying an appropriate mask.
'''

def hash_function(s):
    hash_value = 5381
    current_or = 17 # 5+3+8+1 = 17
    for i in range(2):
        for char in s:
            hash_value = (hash_value * 33) + ord(char)
            hash_value = (hash_value | current_or) << 4
            current_or = ord(char)
    hash_value = hash_value & 0xFFFFFFFF
    return hash_value

input_string = "hello"
print(f"Hash value: {hash_function(input_string)}")
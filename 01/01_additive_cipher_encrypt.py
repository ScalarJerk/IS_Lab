#A python program to illustrate Caesar Cipher Technique
def encrypt(text,shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65) 

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

#check the above function

text = input("\nEnter plaintext\n")
shift = int(input("Enter shift value\n"))   # shift value, i.e. the key value. (when shift = 4, "A" becomes "E", "B" becomes "F")
print ("Text  : " + text)
print ("Shift : " + str(shift))
print ("Cipher: " + encrypt(text,shift))

'''
# inverse character functions can't be used on strings
print(chr(97))
print(ord('a'))
print(chr(ord('a')))
'''
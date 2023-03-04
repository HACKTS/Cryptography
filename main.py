#RESTART THE JOURNEY
print('The first challenge is to apply python into basic CRYPTOGRAPHY')
print('.')
print('.')
print('.')
'pip install cryptography'#i don't think this line is working, will check later


def caesar_cipher(message, shift):
    encrypted_message = ""
    for letter in message:
        if not letter.isalpha():
            encrypted_message += letter
        else:
            if letter.isupper():
                encrypted_letter = chr((ord(letter) - 65 + shift) % 26 + 65)
            else:
                encrypted_letter = chr((ord(letter) - 97 + shift) % 26 + 97)
            encrypted_message += encrypted_letter
    return encrypted_message
message = "fuck this shit"
shift = 4
encrypted_message = caesar_cipher(message, shift)
print(encrypted_message)
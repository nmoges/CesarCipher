# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

ALPHABET = " ABCDFEGHIJKLMNOPQRSTUVWXYZ"
KEY_ENCRYPT = 2


def ceasar_encryption(plain_text):
    encrypt_text = ''
    for letter in plain_text:
        index_letter = ALPHABET.find(letter)
        index_encrypt = (index_letter + KEY_ENCRYPT) % len(ALPHABET)
        encrypt_text = encrypt_text + ALPHABET[index_encrypt]
    return encrypt_text


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':

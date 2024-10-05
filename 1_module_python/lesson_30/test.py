
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encrypt_data(data, key):
    encrypted_data = ""
    for char in data:
        ind = ALPHABET.find(char)
        if ind == -1:
            encrypted_data += char
        else:
            encrypted_data += ALPHABET[(ind + key) % len(ALPHABET)]

    return encrypted_data


def decrypt_data(data, key):
    decrypted_data = ""
    for char in data:
        ind = ALPHABET.find(char)
        if ind == -1:
            decrypted_data += char
        else:
            decrypted_data += ALPHABET[ind - key]

    return decrypted_data


key = 5
data = "hello world"

encrypted_data = encrypt_data(data, key)
print("зашифрованный", encrypted_data)

decrypted_data = decrypt_data(encrypted_data, key)
print("дешифрованный", decrypted_data)


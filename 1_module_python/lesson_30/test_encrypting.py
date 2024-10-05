from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
print(f"secret_key: {secret_key}")

fernet_key = Fernet(secret_key)

data = b'Hello world!'
print(data)

encrypted_data = fernet_key.encrypt(data)
print(f"зашифрованный {data}: {encrypted_data}")

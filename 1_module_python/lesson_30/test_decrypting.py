from cryptography.fernet import Fernet

secret_key = b'HhwPYBkjVpOuq2BHsNHJNh9T8rPkDtRgy5dqn5Gzg3g='
encrypted_data = b'gAAAAABnAVV0Nn55ogWLUJBNYWrotquyBxjWh0kdtcDhAjVJLSMqOPp1TQo5V-tjoqkBBY_GuGZebkxughSSDEsuG34spd_fVA=='

fernet_key = Fernet(secret_key)

decrypted_data = fernet_key.decrypt(encrypted_data)

decrypted_data = decrypted_data.decode()
print(decrypted_data)


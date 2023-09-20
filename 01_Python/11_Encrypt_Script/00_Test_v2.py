from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path + ".enc", 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    cipher = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

# Usage example:
key = generate_key()
encrypt_file("00_test.py", key)
# Remember to securely store the generated key somewhere, you will need it for decryption.

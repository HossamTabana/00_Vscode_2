from cryptography.fernet import Fernet

def generate_and_save_key(key_file):
    """
    Generates a Fernet encryption key and saves it to a file.
    """
    key = Fernet.generate_key()
    with open(key_file, "wb") as keyfile:
        keyfile.write(key)

def load_key_from_file(key_file):
    """
    Loads the Fernet encryption key from a file.
    """
    with open(key_file, "rb") as keyfile:
        key = keyfile.read()
    return key

def encrypt_file(file_path, key):
    """
    Encrypts a file using the provided key.
    """
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path + ".enc", 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    """
    Decrypts a file using the provided key.
    """
    cipher = Fernet(key)
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

# Generate key and save to 'key.key' file
generate_and_save_key("key.key")

# Encrypt file using saved key
key = load_key_from_file("key.key")
encrypt_file("00_test.py", key)

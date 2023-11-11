import pycryptodomex.fernet as fernet

key = fernet.Fernet.generate_key()
print("Generated Key:", key.decode())

# Path to your Python script and the path where you'd like to save the encrypted script
script_path = "C:\\ibrahho\\power.py"
encrypted_script_path = "C:\\ibrahho\\encrypted_power.enc"

encrypt_script(script_path, encrypted_script_path, key)

from cryptography.fernet import Fernet
import hmac
import hashlib
key = Fernet.generate_key()
cipher_suite = Fernet(key)
def constant_time_compare(val1, val2):
    return hmac.compare_digest(val1, val2)
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"File {file_path} encrypted successfully.")
# Decrypt the encrypted file
def decrypt_file(encrypted_file_path):
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    original_file_path = encrypted_file_path.replace('.enc', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {original_file_path} decrypted successfully.")

user_input = input('Enter your password: ')
stored_hash = hashlib.sha256('password123'.encode()).hexdigest()
user_input_hash = hashlib.sha256(user_input.encode()).hexdigest()
encrypt_file('Protect-against-attacks\sensitive_data.txt')

if constant_time_compare(stored_hash, user_input_hash):
    # If the hashes match, authentication is successful
    print("Authentication successful.")
    decrypt_file('Protect-against-attacks\sensitive_data.txt.enc')
else:
    # If the hashes do not match, authentication fails
    print("Authentication failed.")
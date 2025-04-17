import os
import base64
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_key_from_password(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def save_salt(salt_path: str, salt: bytes):
    with open(salt_path, 'wb') as f:
        f.write(salt)

def load_salt(salt_path: str) -> bytes:
    with open(salt_path, 'rb') as f:
        return f.read()

def encrypt_image():
    input_path = input("Enter image file to encrypt: ")
    output_path = input("Enter output file name (e.g., encrypted.img): ")
    password = input("Enter password: ")
    
    salt = os.urandom(16)
    save_salt("salt.salt", salt)
    key = generate_key_from_password(password, salt)
    fernet = Fernet(key)

    try:
        with open(input_path, 'rb') as f:
            data = f.read()

        encrypted = fernet.encrypt(data)

        with open(output_path, 'wb') as f:
            f.write(encrypted)

        print(f"✅ Image encrypted and saved to '{output_path}'")
    except FileNotFoundError:
        print("❌ File not found!")

def decrypt_image():
    input_path = input("Enter encrypted file to decrypt: ")
    output_path = input("Enter output image file name (e.g., output.jpg): ")
    password = input("Enter password: ")

    try:
        salt = load_salt("salt.salt")
        key = generate_key_from_password(password, salt)
        fernet = Fernet(key)

        with open(input_path, 'rb') as f:
            encrypted_data = f.read()

        decrypted = fernet.decrypt(encrypted_data)

        with open(output_path, 'wb') as f:
            f.write(decrypted)

        print(f"✅ Image decrypted and saved to '{output_path}'")
    except FileNotFoundError:
        print("❌ File or salt not found!")
    except Exception:
        print("❌ Wrong password or corrupted file.")

def main():
    while True:
        print("\n🔐 IMAGE ENCRYPTION TOOL")
        print("===========================")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. View Encrypted/Decrypted Images")
        print("4. Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            encrypt_image()
        elif choice == "2":
            decrypt_image()
        elif choice == "3":
            print("\n🖼️ Encrypted/Decrypted Files in Current Directory:")
            for file in os.listdir():
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.img')):
                    print(f" - {file}")
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

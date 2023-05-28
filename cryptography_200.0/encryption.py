import argparse
from cryptography.fernet import Fernet
import os


def generate_key():
    # Generate a new key
    key = Fernet.generate_key()
    return key


def encrypt_file(filepath, key):
    # Read the file to encrypt
    with open(filepath, 'rb') as file:
        original = file.read()

    # Create a Fernet object with the provided key
    fernet = Fernet(key)

    # Encrypt the file
    encrypted = fernet.encrypt(original)

    # Write the encrypted data back to the original file
    with open(filepath, 'wb') as file:
        file.write(encrypted)

    print('\n-----------------|File Encrypted Successfully.|--------------------')
    print('\nENCRYPTION KEY---{Please make sure you keep this key as you\'ll need it decrypt your encrypted file}---:', key.decode())


def main():
    parser = argparse.ArgumentParser(description='File encryption')
    parser.add_argument('filepath', help='Path of the file to encrypt')

    args = parser.parse_args()

    # Generate a new key
    key = generate_key()

    # Save the key to a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    # Encrypt the file using the key
    encrypt_file(args.filepath, key)


if __name__ == '__main__':
    main()


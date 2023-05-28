

import argparse
from cryptography.fernet import Fernet


def decrypt_file(filepath, key):
    # Read the encrypted file
    with open(filepath, 'rb') as file:
        encrypted = file.read()

    # Create a Fernet object with the provided key
    fernet = Fernet(key)

    try:
        # Attempt to decrypt the file
        decrypted = fernet.decrypt(encrypted)

        # Write the decrypted data to a new file
        with open(filepath, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        print('\n--------------------|File Decrypted Successfully.|-------------------------')
    except:
        print('\n*********Decryption failed. Please try again.*****************')



def main():
 parser = argparse.ArgumentParser(description='File decryption')
 parser.add_argument('filepath', help='Path of the file to decrypt')

 args = parser.parse_args()

 key = input('Please enter the decryption key: ')

 # Read the key from the file
 with open('filekey.key', 'rb') as filekey:
   stored_key = filekey.read()

 # Check if the provided key matches the stored key
 while True:
   if key.encode() != stored_key:
     print('\n!!!!!!!!!!!!!!!!Invalid Key. Please Try Again.!!!!!!!!!!!!!!!!!!')
     key = input('\nPlease enter the decryption key: ')
   else:
    break

 # Decrypt the file using the key
 decrypt_file(args.filepath, stored_key)



if __name__ == '__main__':
    main()


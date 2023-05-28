


------------------------------#File Encryption & Decrypotion(Cryptography200.0)#---------------------------------
---------------------------------------------------------------------------------------------------------------
                                          ||| Description |||
 - This is a command-line tool for encrypting and decrypting files using the Fernet encryption algorithm.

 - This project provides a simple way to encrypt and decrypt files using a symmetric encryption algorithm. It generates a key, allows you to encrypt a file with the generated key, and then provides a way to decrypt the file using the same key.

 - Users are to use the same key gotten while Encrypting the file to be able to decrypt the ecrypted file.

 - with an invalid key the user will not be able to decrypt an ecrypted file.

 - A lost key will mean, the encrypted file will remain encrypted forever. (create a back up for your file if you're not sure you're capable of holding on to the key)

 --------------------------------------------------------------------------------------------------------------------------

## Requirements
- Python 3.x/ the latest version

- cryptography library (install using `pip install cryptography`)

---------------------------------------------------------------------------------------------------------------------------

## Installation

1.  Download the Source code(cryptography_200.0)

----------------------------------------------------------------------------------------------------------------------------

## Usage
### Encrypting a File
To encrypt A file follow these steps:

- locate your terminal.
- Make sure you're inside the cryptography_200.0 directory. For example `cd <folderPath> ` i.e the path for cryptograpy_200.0 on your machine.
Mine looks something like this:
|-----------------------------------------------------------------------|
|Last login: Fri May 26 02:15:37 on ttys027                             |
|divine@Divines-MacBook-Pro ~ % cd /Users/divine/cryptography_200.0     |
|divine@Divines-MacBook-Pro cryptography_200.0 %                        |
|-----------------------------------------------------------------------|

- When inside the Folder, use the command line `python3 encryption.py <filepath>` 
- A success output will be seen including an encryption key.(copy the key)


### Decrypting a File
To decrypt A file follow these steps:

- while inside the same folder inside the terminal.
- Use the command line `python3 decryption.py <filepath>` i.e the same file path that was used in the encryption.
- You'll be prompted to input a decryption key. Input the encryption key you copied.
- Success message saying your file is decrypted successfully.

------------------------------------------------------------------------------------------------------------------------------------

                                               ||| File Structure |||
- `encryption.py`: Python script for file encryption.
- `decryption.py`: Python script for file decryption.
- `filekey.key`: The generated encryption key stored in a file.
- `README.md`: Documentation file (you are here right now).


------------------------------------------------------------------------------------------------------------------------------------

## Troubleshooting
- **Issue**: Permission error when trying to encrypt or decrypt a file.
  - **Solution**: Ensure that you have the necessary permissions to read, write, and execute files in the specified directories. You may need to adjust file permissions or run the command with appropriate user privileges.

- **Issue**: Invalid key error when decrypting a file.
  - **Solution**: Double-check that you are entering the correct decryption key. The key must match the one used during the encryption process. If you have lost the key or are unsure, you will not be able to decrypt the file.

- **Issue**: Dependency errors or installation issues.
  - **Solution**: Make sure you have installed Python 3.x and the required `cryptography` library. Try reinstalling the dependencies using 
  `pip install -r requirements.txt` and ensure that the installation completes successfully.

- **Issue**: No such file or directory.
  - **Soluton**: Make sure the file path is correct and the file which you're trying to Encrypt exits in a particular place on your machine.

- **Issue**: Other problems or errors.
  - **Solution**: If you encounter any other issues or errors, please send a text to me with a detailed description of the problem, including any error messages you receive @pAprickA17 on telegram.I will do my best to assist you.

------------------------------------------------------------------------------------------------------------------------------------------

## Acknowledgments
- The project was inspired by the need for a simple file encryption tool just to make confidential information more secure.

- The cryptography library was used for implementing the encryption and decryption functionality.

------------------------------------------------------------------------------------------------------------------------------------------

## Contact
For any inquiries or support, please contact [ Bali ](divinebaly1188@aol.com).








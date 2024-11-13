Caesar and Vigenère Cipher
This repository contains Python implementations of two classic cryptographic algorithms: the Caesar Cipher and the Vigenère Cipher. These are basic encryption techniques that can be used to securely encode and decode messages.

How it works
The program provides an interactive command-line interface where you can choose between the Caesar Cipher or the Vigenère Cipher. Once you select the cipher, you can either encrypt or decrypt a message by entering the required information.

Caesar Cipher
The Caesar Cipher is one of the simplest encryption methods. It works by shifting the letters of the alphabet by a fixed number, called the "shift" or "offset". For example, with a shift of 3, the letter "A" becomes "D", "B" becomes "E", and so on.

Encryption: Each letter in the message is shifted forward by a fixed number of positions in the alphabet.
Decryption: Each letter in the encrypted message is shifted backward by the same number to retrieve the original message.
Vigenère Cipher
The Vigenère Cipher is a more complex encryption algorithm that uses a keyword (or key) to determine the shifting pattern. Each letter of the message is shifted by a number of positions defined by the corresponding letter of the key.

Encryption: The letters in the message are shifted based on the letters of the key. If the key is shorter than the message, it repeats.
Decryption: The decryption process works by reversing the shifts using the same key.
Functions
Caesar Cipher
cryptage_cesar(message, decalage): Encrypts a given message using the Caesar cipher with a specified shift (decalage).
decryptage_cesar(texte_crypte, decalage): Decrypts a given encrypted message using the Caesar cipher and the specified shift (decalage).
Vigenère Cipher
cryptage_vigenere(message, cle): Encrypts a given message using the Vigenère cipher with a specified key (cle).
decryptage_vigenere(texte_crypte, cle): Decrypts a given encrypted message using the Vigenère cipher and the specified key (cle).
Usage
Running the Program
Select a cipher:

Enter 1 for Caesar Cipher or 2 for Vigenère Cipher.
Choose to encrypt or decrypt:

Enter 1 to encrypt a message or 2 to decrypt a message.
Provide the required information:

For the Caesar Cipher: Enter a shift value (decalage) and the message you want to encrypt or decrypt.
For the Vigenère Cipher: Enter the encryption key (cle) and the message you want to encrypt or decrypt.

Code Explanation
The program consists of two main sections:

Caesar Cipher:

The program takes a message, shifts each letter by the specified number (decalage), and returns the encrypted message. It also works in reverse to decrypt the message.
Vigenère Cipher:

The program uses a keyword (cle) to shift each letter of the message. The key is repeated if shorter than the message. It applies the Vigenère encryption and decryption methods.
Code Structure
Caesar Cipher Functions:

cryptage_cesar: Encrypts the message with a shift.
decryptage_cesar: Decrypts the message using the same shift.
Vigenère Cipher Functions:

cryptage_vigenere: Encrypts the message using the Vigenère cipher.
decryptage_vigenere: Decrypts the message using the Vigenère cipher.
User Interface:

The program repeatedly asks the user to choose between encryption or decryption and the cipher to use (Caesar or Vigenère).
Requirements
This program is written in Python 3.x and doesn't have any external dependencies. You just need a Python environment to run it.

License
This project © 2024 by Augustin PIEGAY and Zoe ALBOUY is licensed under CC BY-NC-SA 4.0.

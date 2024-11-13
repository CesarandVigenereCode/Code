# Caesar and Vigenère Cipher

This repository contains Python implementations of two classic cryptographic algorithms: the **Caesar Cipher** and the **Vigenère Cipher**. These are basic encryption techniques that can be used to securely encode and decode messages.

## How it works

The program provides an interactive command-line interface where you can choose between the **Caesar Cipher** or the **Vigenère Cipher**. Once you select the cipher, you can either encrypt or decrypt a message by entering the required information.

### Caesar Cipher

The **Caesar Cipher** is one of the simplest encryption methods. It works by shifting the letters of the alphabet by a fixed number, called the "shift" or "offset". For example, with a shift of 3, the letter "A" becomes "D", "B" becomes "E", and so on.

- **Encryption**: Each letter in the message is shifted forward by a fixed number of positions in the alphabet.
- **Decryption**: Each letter in the encrypted message is shifted backward by the same number to retrieve the original message.

### Vigenère Cipher

The **Vigenère Cipher** is a more complex encryption algorithm that uses a keyword (or key) to determine the shifting pattern. Each letter of the message is shifted by a number of positions defined by the corresponding letter of the key.

- **Encryption**: The letters in the message are shifted based on the letters of the key. If the key is shorter than the message, it repeats.
- **Decryption**: The decryption process works by reversing the shifts using the same key.

## Functions

### Caesar Cipher

- `cryptage_cesar(message, decalage)`: Encrypts a given message using the Caesar cipher with a specified shift (`decalage`).
- `decryptage_cesar(texte_crypte, decalage)`: Decrypts a given encrypted message using the Caesar cipher and the specified shift (`decalage`).

### Vigenère Cipher

- `cryptage_vigenere(message, cle)`: Encrypts a given message using the Vigenère cipher with a specified key (`cle`).
- `decryptage_vigenere(texte_crypte, cle)`: Decrypts a given encrypted message using the Vigenère cipher and the specified key (`cle`).

## Usage

### Running the Program

1. **Select a cipher**: 
   - Enter `1` for Caesar Cipher or `2` for Vigenère Cipher.

2. **Choose to encrypt or decrypt**:
   - Enter `1` to encrypt a message or `2` to decrypt a message.

3. **Provide the required information**:
   - For the Caesar Cipher: Enter a shift value (`decalage`) and the message you want to encrypt or decrypt.
   - For the Vigenère Cipher: Enter the encryption key (`cle`) and the message you want to encrypt or decrypt.

### Code Explanation
The program consists of two main sections:
1. **Caesar Cipher**: 
   - The program takes a message, shifts each letter by the specified number (decalage), and returns the encrypted message. It also works in reverse to decrypt the message.

2. **Vigenère Cipher**:
   - The program uses a keyword (cle) to shift each letter of the message. The key is repeated if shorter than the message. It applies the Vigenère encryption and decryption methods.

# Encryption Program: Caesar & Vigenère Ciphers

This program provides two encryption methods: the Caesar cipher and the Vigenère cipher. Users can encrypt and decrypt messages using these ciphers, either with a specified shift (for Caesar) or a keyword (for Vigenère).

## Code Explanation

### Caesar Cipher
- **Encryption:** The program shifts each letter of the message by a specified number (the shift value or `décalage`), and returns the encrypted message.
- **Decryption:** It also works in reverse, using the same shift value to decrypt the message.

### Vigenère Cipher
- **Encryption:** The program uses a keyword (`cle`) to shift each letter of the message. If the keyword is shorter than the message, it is repeated to match the length of the message. The encryption follows the Vigenère method.
- **Decryption:** The program can also decrypt messages that were encrypted with the Vigenère cipher by applying the reverse shift according to the keyword.

## Code Structure

### Caesar Cipher Functions:
- **`cryptage_cesar(message, decalage)`**: Encrypts the message using a Caesar cipher with the specified shift (`décalage`).
- **`decryptage_cesar(message, decalage)`**: Decrypts the message using the same Caesar cipher shift.

### Vigenère Cipher Functions:
- **`cryptage_vigenere(message, cle)`**: Encrypts the message using the Vigenère cipher with the provided keyword (`cle`).
- **`decryptage_vigenere(message, cle)`**: Decrypts the message using the Vigenère cipher and the same keyword.

### User Interface
- The program repeatedly prompts the user to choose between encryption or decryption and to select the cipher they wish to use (Caesar or Vigenère). The user then provides the required parameters (shift value or keyword) to complete the operation.

## Requirements
This program is written in **Python 3.x** and has no external dependencies. You only need a Python environment to run it.

## Installation
To get started, clone this repository:

```bash
git clone https://github.com/yourusername/encryption-program.git
```
```bash
cd encryption-program
```

## License
Code César et Vigenère © 2024 by Augustin PIEGAY and Zoe ALBOUY is licensed under CC BY-NC-SA 4.0. 
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

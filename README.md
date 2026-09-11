# OTP Encryption CLI Tool

A simple and lightweight Command-Line Interface (CLI) tool written in Python for encrypting and decrypting text based on the **One-Time Pad (OTP)** cipher principle.

## Features

- **Cryptographically Secure Keys:** Key generation uses Python's `secrets` module (a cryptographically secure pseudorandom number generator).
- **Printable ASCII Range:** Encryption is constrained to printable ASCII characters (Modulo 95), allowing both key and ciphertext to remain in human-readable text format.
- **Flexible Input/Output Handling:**
  - Manual input of text and keys directly in the terminal.
  - Automated file reading from `.txt` files (supports drag-and-drop file paths).
  - Export keys and ciphertext to text files labeled with unique timestamps (`YYYY-MM-DD-HH-MM-SS`).

## How It Works

The script applies a shift cipher over the range of printable ASCII characters (values 32 through 126):

1. **Encryption:**  
   $$\text{Cipher} = ((\text{Char} - 32 + \text{Key}) \bmod 95) + 32$$
2. **Decryption:**  
   $$\text{Plain} = ((\text{Cipher} - 32 - \text{Key}) \bmod 95) + 32$$

> **Security Note:** A One-Time Pad is mathematically unbreakable, provided the key is **truly random**, **at least as long as the message**, and **never reused**.

## Installation & Usage

1. Clone this repository or download `main.py`.
2. No external dependencies are required (uses Python Standard Library only).
3. Run the application:
4.~ python main.py

(ReadMe written by AI;
code written by me)

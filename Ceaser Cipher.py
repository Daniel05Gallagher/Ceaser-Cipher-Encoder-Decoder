import string
# Base instance variables
alphabet = string.ascii_lowercase


# Progam open
print()
print("--- Ceaser Cipher Tool ---")
print()
print("Type [Encode] or [Decode] to continue to the appropriate mode")
user_in = input("Input: ").lower()

# Encoding Tool
if user_in == "encode":
    print("--- Encoding Tool Selected ---")
    print()
    key = int(input("Enter a encryption key between 1-26: "))
    plaintext = input("Enter your text that you wish encoded: ").lower()
    cipher = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, cipher)
    encoded = plaintext.translate(table)
    print(encoded)

# Decoding Tool
if user_in == "decode":
    print("--- Decoding Tool Selected ---")
    print()
    key = int(input("Enter a decryption key between 1-26: "))
    plaintext = input("Enter your text that you wish decoded: ").lower()
    key = 26-key
    cipher = alphabet[key:] + alphabet[:key]
    table = str.maketrans(alphabet, cipher)
    decoded = plaintext.translate(table)
    print(decoded)


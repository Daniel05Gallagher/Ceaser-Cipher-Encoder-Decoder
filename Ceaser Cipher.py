import string
alphabet = string.ascii_lowercase

# Encoding function
def encode(keyIn, plaintextIn):
    cipher = alphabet[keyIn:] + alphabet[:keyIn]
    table = str.maketrans(alphabet, cipher)
    encoded = plaintextIn.translate(table)
    print(encoded)
    
# Decoding function
def decode(keyIn, plaintextIn):
    cipher = alphabet[keyIn:] + alphabet[:keyIn]
    table = str.maketrans(alphabet, cipher)
    decoded = plaintextIn.translate(table)
    print(decoded)

# Progam open
print()
print("--- Ceaser Cipher Tool ---")
print()
print("Type [Encode] or [Decode] to continue to the appropriate mode")
user_in = input("Input: ").lower()

# Encoding Tool
if user_in == "encode":
    print()
    print("--- Encoding Tool Selected ---")
    print()
    key = int(input("Enter a encryption key between 1-26: "))
    plaintext = input("Enter your text that you wish encoded: ").lower()
    encode(key, plaintext)

# Decoding Tool
if user_in == "decode":
    print()
    print("--- Decoding Tool Selected ---")
    print()
    key = int(input("Enter a decryption key between 1-26: "))
    plaintext = input("Enter your text that you wish decoded: ").lower()
    key = 26-key
    decode(key, plaintext)
    
else:
    exit


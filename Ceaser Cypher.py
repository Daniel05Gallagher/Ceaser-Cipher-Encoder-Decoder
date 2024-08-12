import string
# Base instance variables
alphabet = string.ascii_lowercase+string.ascii_uppercase

# Encoding function
def encode(keyIn, plaintextIn):
    cypher = alphabet[keyIn:] + alphabet[:keyIn]
    table = str.maketrans(alphabet, cypher)
    encoded = plaintextIn.translate(table)
    print(encoded)
    
# Decoding function
def decode(keyIn, plaintextIn):
    cypher = alphabet[keyIn:] + alphabet[:keyIn]
    table = str.maketrans(alphabet, cypher)
    decoded = plaintextIn.translate(table)
    print(decoded)

# Progam open
print()
print("--- Ceaser cypher Tool ---\n")
print("Type [Encode] or [Decode] or [Bruteforce] to continue to the appropriate mode")
user_in = input("Input: ").lower()

# Encoding Tool
if user_in == "encode":
    print()
    print("--- Encoding Tool Selected ---\n")
    key = int(input("Enter a encryption key between 1-26: "))
    plaintext = input("Enter your text that you wish encoded: ").lower()
    encode(key, plaintext)

# Decoding Tool
if user_in == "decode":
    print()
    print("--- Decoding Tool Selected ---\n")
    key = int(input("Enter a decryption key between 1-26: "))
    plaintext = input("Enter your text that you wish decoded: ").lower()
    key = 26-key
    decode(key, plaintext)
    
# Bruteforce Tool
if user_in == "bruteforce":
    print()
    print("--- Bruteforcing Decoding Tool Selected ---\n")
    plaintext = input("Enter your text that you wish brutefroce decoded: ").lower()
    
    # For loop to run though each possible key and print the output
    for i in range(26):
        key = i
        decode(key, plaintext)
    
else:
    exit


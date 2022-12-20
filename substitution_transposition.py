import random

def substitution_cipher(plaintext, key):
    # Create a dictionary that maps each letter to a different letter
    mapping = {}
    for i in range(len(key)):
        mapping[key[i]] = plaintext[i]
    # Use the mapping to encode the plaintext
    ciphertext = ""
    for c in plaintext:
        ciphertext += mapping[c]
    return ciphertext

def transposition_cipher(plaintext, key):
    # Create a list of tuples that represents the original order of the characters
    order = [(key[i], c) for i, c in enumerate(plaintext)]
    # Sort the list of tuples based on the key
    order.sort(key=lambda x: x[0])
    # Rebuild the plaintext using the sorted list of tuples
    ciphertext = "".join([c for k, c in order])
    return ciphertext

def decrypt(ciphertext, key):
    # Reverse the process of the cipher to obtain the original plaintext
    if len(key) == len(ciphertext):
        # Substitution cipher
        mapping = {}
        for i in range(len(key)):
            mapping[ciphertext[i]] = key[i]
        plaintext = ""
        for c in ciphertext:
            plaintext += mapping[c]
    else:
        # Transposition cipher
        order = [(key[i], c) for i, c in enumerate(ciphertext)]
        order.sort(key=lambda x: x[0])
        plaintext = "".join([c for k, c in order])
    return plaintext

# Generate a random key for the substitution cipher
key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
random.shuffle(key)
key = "".join(key)

# Get the plaintext from the user
plaintext = input("Enter the plaintext: ")

# Encode the plaintext using the substitution cipher
ciphertext = substitution_cipher(plaintext, key)
print("Substitution Cipher:")
print("Key:", key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext to obtain the original plaintext
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)

# Encode the plaintext using the transposition cipher
key = input("Enter the key for the transposition cipher: ")
ciphertext = transposition_cipher(plaintext, key)
print("\nTransposition Cipher:")
print("Key:", key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext to obtain the original plaintext
plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)

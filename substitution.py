import string

def substitution_cipher(plaintext, key):
    # Create a translation table to map each character to its corresponding
    # character in the key.
    table = str.maketrans(string.ascii_lowercase, key)

    # Use the translation table to map each character in the plaintext to its
    # corresponding character in the key, resulting in the ciphertext.
    ciphertext = plaintext.lower().translate(table)

    return ciphertext

# Test the substitution cipher
plaintext = "attack at dawn"
key = "zxcvbnmlkjhgfdsaqwertyuiop"
ciphertext = substitution_cipher(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")

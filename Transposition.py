def transposition_cipher(plaintext, key):
    # Create a list of the characters in the plaintext, sorted according to
    # the order specified by the key
    sorted_chars = [x for _, x in sorted(zip(key, plaintext))]

    # Concatenate the sorted characters to form the ciphertext
    ciphertext = "".join(sorted_chars)

    return ciphertext

# Test the transposition cipher
plaintext = "attack at dawn"
key = "53214"
ciphertext = transposition_cipher(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Ciphertext: {ciphertext}")

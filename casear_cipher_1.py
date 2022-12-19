def shift_char(char, shift):
    """Shift a single character by the specified amount."""
    if char.isalpha():
        # convert the character to uppercase to simplify the shifting
        char = char.upper()
        # shift the character by the specified amount
        char = chr((ord(char) + shift - 65) % 26 + 65)
        # if the original character was lowercase, convert the shifted character back to lowercase
        if char.isupper():
            char = char.lower()
    return char

def caesar_cipher(plaintext, shift):
    """Encode a string using the Caesar Cipher."""
    # create a string to store the ciphertext
    ciphertext = ""
  
    # iterate through each character in the plaintext
    for char in plaintext:
        # shift the character and add it to the ciphertext
        ciphertext += shift_char(char, shift)
  
    # return the ciphertext
    return ciphertext

# prompt the user for the plaintext and shift value
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift value: "))

# use the Caesar Cipher to generate the ciphertext
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)

# to obtain the plaintext, just shift the ciphertext back by the same amount
plaintext = caesar_cipher(ciphertext, -shift)
print("Plaintext:", plaintext)

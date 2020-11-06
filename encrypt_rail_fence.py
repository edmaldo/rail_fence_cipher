"""Encrypt a Civil War 'rail fence' style cipher.


Example message ===                     'Buy more sweet potatoes'

Separate letters in zigzag rows ===         \/\/\/\//\/\/\

Rail fence style ===                     B Y O E W E P T T E
                                          U M R S E T O A O S

Make one line ciphertext starting with top row and finishing with second row

ciphertext becomes === BYOEW EPTTE UMRSE TOAOS

"""
#----------------------------------------------------------

# Enter message to be encrypted
plaintext = 'Let us cross over the river and rest under the shade of the trees'

#-----------------------------------------------------------


def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def prep_plaintext(plaintext):
    """Remove spaces and leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()
    print(f"\nplaintext = {plaintext}")
    return message


def build_rails(message):
    """Build strings with every other letter in a message."""
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    """Split letters in ciphertext inot chucks of 5 and join to make a string."""
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print(f"ciphertext = {ciphertext}")


if __name__ == '__main__':
    main()

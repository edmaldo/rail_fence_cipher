"""Decrypt the ciphertext by untangling rail fence style cipher.

Now that you have a cryptic message, you must untangle it.

Ciphertext from encryption ===   BYOEW EPTTE UMRSE TOAOS

Start from middle of ciphertext to create two rows ===

                                    BYOEWEPTTE
                                    UMRSETOAOS

Connect rows in zigzag style ===   \/\/\/\/\/\/\

End with ===                    BUYMORESWEETPOTATOES

'Buy more sweet potatoes'

"""
import math
import itertools

ciphertext = 'LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES'


def main():
    """Run program to decrypt 2-rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)


def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print(f"ciphertext = {ciphertext}\n")
    return message


def split_rails(message):
    """Split message in two, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()
    return row1, row2


def decrypt(row1, row2):
    """Build list with every other letter in 2 strings and print."""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    print(f"rail 1 = {row1}")
    print(f"rail 2 = {row2}")
    print(f"\nplaintext = {''.join(plaintext)}")


if __name__ == '__main__':
    main()

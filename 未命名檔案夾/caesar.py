"""
File: caesar.py
Name: Alyssa (2hr)
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""

# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program deciphers the string which users input
    a number and an encrypted string which translated by
    the number.
    """
    n = int(input('Secret number: '))
    a = str(input("What's the ciphered string?"))
    print('The decipered string is: '+deciper(a,n))


def deciper(a,n):
    ans=''
    a1 = a.upper()
    for i in range(len(a1)):
        if ALPHABET.find(a1[i]) == -1:
            ans += a1[i]
        elif ALPHABET.find(a1[i])+n >= 26:
            ans += ALPHABET[ALPHABET.find(a1[i])+n-26]
        else:
            ans += ALPHABET[ALPHABET.find(a1[i])+n]
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

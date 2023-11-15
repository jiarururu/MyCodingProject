"""
File: complement.py
Name: Alyssa (0.5hr)
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program finds the complement strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans=""
    for i in range(len(dna)):
        if dna[i] == 'A':
            ans += 'T'
        if dna[i] == 'T':
            ans += 'A'
        if dna[i] == 'C':
            ans += 'G'
        if dna[i] == 'G':
            ans += 'C'
    if dna == "":
        ans += 'DNA strand is missing.'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

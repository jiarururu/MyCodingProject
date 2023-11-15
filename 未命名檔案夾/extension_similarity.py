"""
File: similarity.py (extension)
Name: ALyssa (3hr)
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program can identify the interval within a longer DNA sequence
    where a short DNA sequence has the highest matching rate,
    which both DNA sequences are input by users.
    """
    dna = str(input('Please give me a DNA sequence to search: ')).upper()
    p = str(input('What DNA sequence would you like to match? ')).upper()
    a = len(dna)-len(p)+1         #how many sets of DNA sequences to be tested
    r = 0       #matching rate
    ans = ''
    for i in range(a):
        correct = dna[i:i+len(p)]
        if probability(correct,p) >= r:
            r = probability(correct,p)
            ans = correct
    print('The best match is '+ans)


def probability(correct,p):         #the matching rate of sets of DNA sequences
    count = 0
    for alpha in range(len(p)):
        if p[alpha] == correct[alpha]:
            count += 1
    return count


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

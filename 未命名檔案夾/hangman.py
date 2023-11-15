"""
File: hangman.py
Name: Alyssa
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a game that users guess each character in
    a random word with dashed, while guessed correct ,the alphabet
    will replace the dashed.(users get N_TURNS chances)
    """
    r = N_TURNS
    a = random_word()
    current = dashed(a)
    print('The word looks like ' + current)
    print('You have ' + str(r) + ' wrong guesses left.')
    while True:
        n = str(input('Your guess: ')).upper()
        current = new(a, n, current)     #keep the lastest one
        if not n.isalpha() or len(n) >1:
            print('Illegal format.')
        else:
            if n in a:
                print('You are correct!')
                if current == a:
                    print('You win!!')
                    print('The word was: ' + a)
                    break
            else:
                print('There is no '+ n +'\'s in the word.')
                r -= 1
                if r == 0:
                    print('You are completely hung : (')
                    print('The word was: ' + a)
                    break
            print('The word looks like ' + current)
            print('You have ' + str(r) + ' wrong guesses left.')


def dashed(a):        #the characters of answer covered by dashed
    ans=''
    for i in a:
        ans += '-'
    return ans


def new(a, n, current):      #replace dashed with correct alphabet which users input
    ans=''
    for i in range(len(a)):
        if a[i] != n:
            ans += current[i]
        else:
            ans += n
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

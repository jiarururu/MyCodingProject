"""
File: name_sq.py (extension)
Name: Alyssa (2hr)
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main() :
    """
    The users input a string, this program will print
    a square which surrounded by the string.
    """
    print('This program prints a name in a square pattern!')
    n = str(input('Name: '))
    a = len(n)
    for i in range(a):
        if i == 0:           #first full name
            print(n)
        if i == a-1:
            print(reverse(n))
        elif i < a-2:               #the middle of square
                print(n[i+1]+' '*(a-2)+n[a-i-2])
                i += 1


def reverse(n):             #last reverse name
    result = ''
    for i in range(len(n)):
        result = n[i]+result
    return result


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()

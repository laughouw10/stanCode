"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    cut and make a new alphabet order
    match and print
    """
    num = int(input("enter secret number: "))
    new_order = ALPHABET[26-num:] + ALPHABET[:26-num]  # make the new order of alphabet with the secret number entered
    caesar = input("What is the Cipher string? ")
    caesar = caesar.upper()  # deal with the case-sensitive issue
    ans = ""
    for i in range(len(caesar)):
        for j in range(26):
            if caesar[i].isalpha():  # for each alphabet in the "Caesar" entered, find the location(number) it new_order
                if caesar[i] == new_order[j]:  # use the number found to print the real message using the original order
                    ans += ALPHABET[j]
                elif caesar[i] == " ":
                    ans += " "
            else:
                ans += caesar[i]
                break
    print(ans)


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()

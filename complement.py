"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO:
    input DNA sequence
    output the complement of the entered DNA sequence
    """
    build_complement()
    pass


def build_complement():
    k = input("please enter: ")
    k = k.upper()  # case-insensitive
    ans = ""
    for i in range(len(k)):  # match the DNA sequence
        if k[i] == "A":
            ans += "T"
        if k[i] == "T":
            ans += "A"
        if k[i] == "G":
            ans += "C"
        if k[i] == "C":
            ans += "G"
    print(ans)

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO:
    enter 2 DNA sequences
    one to be searched and one to be matched
    output the result with the highest similarity
    """
    ans = ""
    long_seq = input("please give a DNA sequence to search: ")
    a = long_seq.upper()  # input and deal with the case-insensitive
    short_seq = input("What DNA sequence you want to match? ")
    b = short_seq.upper()
    m = 0
    for i in range(len(a)-len(b)+1):  # calculate the time to be tested
        c = long_seq[i:len(b)+i]      # cut the DNA sequence to be searched(longer one) to a proper length
        for j in range(len(b)):
            n = 0
            if c[j] == b[j]:          # if it is a match, put a number on "n"
                n += 1
        if n > m:
            m = n                     # 'm' judges which is the sequence part has the highest similarity
            ans = c                   # assign to ans and print the result
    print(ans)




###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()

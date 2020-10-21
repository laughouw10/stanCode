"""
File: anagram.py
Name: Peter
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
Python_list = []
word = ''
word_list = []
count = 0


def main():
    # create an inout format
    # enter recursion
    # print final result with the word count
    global word_list, count
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        word_input = input('find anagram for: ')

        if word_input == EXIT:
            break

        else:
            print("Searching ...")
            find_anagrams(word_input)
            print(count, 'anagrams', word_list)
            count = 0
            word_list = []


def read_dictionary():
    # read dictionary and put data into into a created python list
    global Python_list
    with open(FILE, "r") as f:
        for data in f:
            Python_list += data.split()


def find_anagrams(s):
    global word, word_list, count
    # print(s, word)
    """
    :param s: the input word
    :return: print word if founded in the dictionary
    """
    # base case, print, count, and add the word into word_list
    if len(s) == 0:
        if word in Python_list and word not in word_list:
            print("Found:  ", word)
            print("Searching ...")
            count += 1
            word_list.append(word)

    # Backtracking
    else:
        for i in range(len(s)):
            if has_prefix(word) is True:
                word += s[i]
                s1 = s[:i] + s[i + 1:]
                find_anagrams(s1)
                word = word[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: the current searching word
    :return: if the word search needs to continue to stop (T/F)
    """
    for word in Python_list:
        if word.startswith(sub_s):
            return True
    return False


"""
def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        word_input = input('find anagram for: ')

        if word_input == EXIT:
            break

        else:
            find_anagrams(word_input)


def read_dictionary():
    global Python_list
    with open("dictionary.txt", "r") as f:
        for data in f:
            Python_list += data.split()



"""
"""
def find_anagrams(s):
    global word

    :param s:
    :return:

    if len(s) == 0:
        if word in Python_list:
            print("Searching ...")
            print(word)


    else:
        for i in range(len(s)):
            word += s[i]
            print(word)
            k = s[i]
            if len(s) == 1:
                s1 = ''
            else:
                s1 = s[:i] + s[i+1:]
            find_anagrams(s1)
"""




"""
def has_prefix(sub_s):
    """



if __name__ == '__main__':
    main()

"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


SIZE = 3


def main():  # decomposition
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        ans = " "  # empty sting
        for k in range(SIZE-i-1):  # put space on the left to make a triangle
            ans += " "             # SIZE = the height of head = (space on the left + i)
        for l in range(i+1):       # put "/" on the left to built the head (i will start from 0, so use range(i+1))
            ans += "/"
        for m in range(i+1):       # put "\" on the right
            ans += "\\"
        for n in range(SIZE-i-1):
            ans += " "
        print(ans)


def upper():  # same concept of "head" part
    for i in range(SIZE):
        ans = "|"
        for j in range(SIZE-i-1):
            ans += "."
        for k in range(i+1):
            ans += "/\\"
        for j in range(SIZE-i-1):
            ans += "."
        ans += "|"
        print(ans)


def lower():
    for i in range(SIZE):
        ans = "|"
        for j in range(i):
            ans += "."
        for k in range(SIZE-i):
            ans += "\\/"
        for j in range(i):
            ans += "."
        ans += "|"
        print(ans)



def belt():
	ans = ""
	ans += "+"
	for i in range(SIZE*2):
		ans += "="
	ans += "+"
	print(ans)






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
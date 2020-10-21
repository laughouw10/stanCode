"""
File: boggle.py
Name: Peter
----------------------------------------
TODO:
	create a "boggle" to match every exist vocabs in the dictionary with the 4x4 character input
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []
word_list = []
count = 0
# all = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]

def main():
	"""
	TODO:
	create a "boggle" to match every exist vocabs in the dictionary with the 4x4 character input
	"""
	read_dictionary()
	List = []
	# input the 4x4 character and fix illegal format as well as case sensitive
	for i in range(4):
		letters = input(str(i+1) + " row of letters: ")
		list = []
		for j in range(4):
			list += letters[(2 * j)].lower()
		List.append(list)
		if len(letters) != 7:
			print("Illegal input")
			break

	# loop every input character as the first character in the word
	# enter the find_word recursion
	# print final result
	for i in range(4):
		for j in range(4):
			word = List[i][j]
			cor_list = [(i, j)]
			find_word(List, i, j, word, cor_list)
			cor_list.clear()
	print("There are", count, "word(s) in total.")


def find_word(l, m, n, word, cor_list):
	global word_list, count
	# base case
	if word in dictionary and len(word) > 3 and word not in word_list:
		print('Found: ', word)
		word_list.append(word)
		count += 1

	# to solve the "room" "roomy" problem, we can not add "else" here
	# use double for loop to run every possibility on the 4x4 input
	# and use has_prefix to cut
	if has_prefix(word) is True:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 4 > m+i >= 0 and 4 > n+j >= 0 and (m+i, n+j) not in cor_list:
					word += l[m+i][n+j]
					cor_list.append((m+i, n+j))
					find_word(l, m+i, n+j, word, cor_list)
					cor_list.pop()
					word = word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary
	with open(FILE, "r") as f:
		for words in f:
			dictionary += words.split()



def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

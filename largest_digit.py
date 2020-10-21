"""
File: largest_digit.py
Name: Peter
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
biggest_num = 0
num = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	global num, biggest_num
	# fix negative input
	if n < 0:
		n = -n
	# base case, return biggest digit
	if n == 0:
		k = biggest_num
		biggest_num = 0
		return k

	# check the digit one by one from the units digit
	else:
		num = n % 10
		if biggest_num < num:
			biggest_num = num
		return find_largest_digit(n // 10)







if __name__ == '__main__':
	main()

"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	# Base Case
	if n < 0:
		n = -n
	if (n/10) < 1:  # 當只剩個位
		return n
	# Self-Similarity
	else:  # 在還有至少兩個位數的情況下
		one = n - int(n/10)*10  # 獲得個位數值
		tens = int(n/10)  # 獲得十位數值以上=捨去個位
		ten = tens - int(tens/10)*10  # 獲得十位數值
		if one > ten:  # 當個位數值大於十位數值
			n = int(tens/10)*10 + one  # 把n中的十位數值移除
		else:
			n = int(n/10)  # 把n中的個位數值移除
		return find_largest_digit(n)


if __name__ == '__main__':
	main()

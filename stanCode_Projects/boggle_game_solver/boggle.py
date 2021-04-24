"""
File: boggle.py
Name:Cherry
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dic = {}


def main():
	"""
	TODO:
	1.get dictionaries, the first letter is the key
	2.let user print 16 characters, get them in the list
	3.let every letter can be the start
	4.find the suit second, third, forth letter
	"""
	# 1.get dictionaries, the first letter is the key
	read_dictionary()
	# 2.let user print 16 characters, get them in the list
	num_list = input_num()
	count = 0
	# 3.let every letter can be the start
	# 每個字母都可以當到開頭
	for groups in range(4):
		for word in range(4):
			ans = []

			# 4.find the suit second, third, forth letter
			# 取周圍一次
			for around1 in [-1, 0, 1]:
				g_around = groups + around1
				if 3 >= g_around >= 0:
					for around2 in [-1, 0, 1]:
						w_around = word + around2
						if 3 >= w_around >= 0:
							used = [(groups, word)]
							switch = 0
							for j in range(len(used)):
								if not (g_around, w_around) == used[j]:
									switch += 0
								else:
									switch += 1
							if switch == 0:

								# 取周圍第二次
								used = [used[0]]
								for around1 in [-1, 0, 1]:
									g_around2 = g_around + around1
									if 3 >= g_around2 >= 0:
										for around2 in [-1, 0, 1]:
											w_around2 = w_around + around2
											if 3 >= w_around2 >= 0:
												if (g_around, w_around) not in used:
													used += [(g_around, w_around)]
												switch = 0
												for i in range(len(used)):
													if not (g_around2, w_around2) == used[i]:
														switch += 0
													else:
														switch += 1
												if switch == 0:

													# 取周圍第三次
													used = used[0:2]
													for around1 in [-1, 0, 1]:
														g_around3 = g_around2 + around1
														if 3 >= g_around3 >= 0:
															for around2 in [-1, 0, 1]:
																w_around3 = w_around2 + around2
																if 3 >= w_around3 >= 0:
																	if (g_around2, w_around2) not in used:
																		used += [(g_around2, w_around2)]
																	switch = 0
																	for i in range(len(used)):
																		if not (g_around3, w_around3) == used[i]:
																			switch += 0
																		else:
																			switch += 1
																	if switch == 0:
																		s = num_list[groups][word] + num_list[g_around][
																			w_around] + num_list[g_around2][w_around2]+\
																			num_list[g_around3][w_around3]
																		if s in dic[s[0]]:
																			if s not in ans:
																				count += 1
																				ans += [s]
																				print(used)
																				print("Found \"" + s + "\"")
	print("There are " + str(count) + " words in total.")


# 	2.let user print 16 characters, get them in the list
def input_num():
	num_list = []
	# 輸入16個字母
	for i in range(4):
		# 確認使用者輸入格式正確
		while True:
			num_str = input(str(i + 1) + " row of letters: ").lower()
			switch = 0
			if len(num_str) == 7:
				for j in range(7):
					if j in [0, 2, 4, 6]:
						if not num_str[j].isalpha():
							switch = 1
					elif j in [1, 3, 5, 7]:
						if not num_str[j] == " ":
							switch = 1
				if switch == 0:
					break
				elif switch == 1:
					print("Illegal input")
			else:
				print("Illegal input")
		# 如果格式正確，放入list中
		num_list += [num_str.split(" ")]
	return num_list


# 	1.get dictionaries, the first letter is the key
def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic
	with open(FILE, "r") as f:
		for word in f:
			sub = word[0:1]
			word = word[:"\n".find(word)]
			if sub in dic:
				dic[sub] += [word]
			else:
				dic[sub] = []
				dic[sub] += [word]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	pass


if __name__ == '__main__':
	main()

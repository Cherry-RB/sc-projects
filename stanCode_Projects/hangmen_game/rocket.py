"""
File: rocket.py
Name:Cherry
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 10  # (if SIZE=1)


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(SIZE):  # i = 0,1,2  		(if SIZE = 1, i = 0)
		for j in range(SIZE-i):  # j = 4,3,2    (j = 1)
			print(' ', end='')
		for k in range(i+1):  # k = 1,2,3       (k = 1)
			print('/', end='')
		for m in range(i+1):  # m = 1,2,3 		(m = 1)
			print('\\', end='')
		print(' ')


def belt():
	print('+', end='')
	for i in range(SIZE*2):
		print('=', end='')
	print('+')


def upper():
	for i in range(SIZE):  # i = 0,1,2  		(if SIZE = 1, i = 0)
		print('|', end='')
		for j in range(SIZE-1-i):  # j = 2,1,0  (j = 0)
			print('.', end='')
		for k in range(i+1):  # k = 1,2,3  		(k = 1)
			print('/\\', end='')
		for m in range(SIZE-1-i):  # m = 2,1,0  (m = 0)
			print('.', end='')
		print('|')


def lower():
	for i in range(SIZE):  # i = 0,1,2  		(if SIZE = 1, i = 0)
		print('|', end='')
		for j in range(i):  # j = 0,1,2  		(j = 0)
			print('.', end='')
		for k in range(SIZE-i):  # k = 3,2,1  	(k = 1)
			print('\\/', end='')
		for m in range(i):  # m = 0,1,2  		(m = 0)
			print('.', end='')
		print('|')



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
"""
File: quadratic_solver.py
Name:Cherry
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
	"""
	TODO(step):
	1.Let user input 3 number,and use 'b*b-4*a*c' to get discriminant
	2.To judge the discriminant is bigger,smaller,or equal with 0 ,and calculate roots
	"""
	print('stanCode Quadratic Solver!')
	# step1.let user input 3 number
	a = int(input('Enter a:'))
	b = int(input('Enter b:'))
	c = int(input('Enter c:'))
	# use 'b*b-4*a*c' to get discriminant
	discriminant = b*b-4*a*c
	# step2.to judge the discriminant is bigger,smaller,or equal with 0
	if discriminant < 0:
		print('No real roots')
	else:
		# calculate roots
		x1 = (-b + math.sqrt(discriminant)) / 2 * a
		x2 = (-b - math.sqrt(discriminant)) / 2 * a
		if discriminant > 0:
			print('Two roots:'+str(x1)+' , '+str(x2))
		else:
			print('One root:'+str(x1))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

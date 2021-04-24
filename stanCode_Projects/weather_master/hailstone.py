"""
File: hailstone.py
Name:Cherry
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO(step):
    1.Let user input one number,and define the variable of step.
    2.Judge the number is even or odd,calculate it until becoming 1.(while)
      (Once calculating,the variable of step +1.)
    3.Print the result.
    """
    print('This program computes Hailstone sequences.')
    print('')
    # step1.Let user input one number.
    n = int(input('Enter a number: '))
    # define the variable of step
    step = 0
    while True:
        # step2.Judge the number is even or odd,and calculate it until becoming 1.
        if n == 1:
            break
        # even
        elif n % 2 == 0:
            print(str(n)+' is even, so I take half: ', end='')
            n = int(n/2)
            print(str(n))
            step += 1  # once calculating,the variable of step +1
        # odd
        elif n % 2 == 1:
            print(str(n) + ' is odd, so I make 3n+1: ', end='')
            n = int(n*3 + 1)
            print(str(n))
            step += 1  # once calculating,the variable of step +1
    # step3.Print the result.
    print('It took '+str(step)+' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()

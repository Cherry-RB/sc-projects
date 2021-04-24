"""
File: weather_master.py
Name:Cherry
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
LEAVING = -1


def main():
	"""
	TODO(step):
	1.Let user input one data.If the data is LEAVING,there are no temperatures.
	2.Define variables:highest,lowest,average,amount,and cold_day.
	3.Let user continuously input data until the data is LEAVING.(while)
	4.Redefine the variables.
	5.Print the results:Highest temperature,Lowest temperature,Average,and cold day(s).
	"""
	print('stanCode "Weather Master 4.0"!')
	# step1.Let user input one data.
	data = int(input('Next Temperature: (or -100 to quit)? '))
	# If the data is LEAVING,there are no temperatures.
	if data == LEAVING:
		print('No temperatures were entered.')
	else:
		# step2.Define variables:highest,lowest,average,amount,and cold_day.
		highest = data
		lowest = data
		average = float(data)
		amount = 1
		if data < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			# step3.Let user continuously input data until the data is LEAVING.
			data = int(input('Next Temperature: (or -100 to quit)? '))
			if data == LEAVING:
				break
			else:
				# step4.Redefine the variables.
				average = average*amount + data
				amount += 1
				average = average/amount
				if data > highest:
					highest = data
				if data < lowest:
					lowest = data
				if data < 16:
					cold_day += 1
		# step5.Print the results:Highest temperature,Lowest temperature,Average,and cold day(s).
		print('Highest temperature = ' + str(highest))
		print('Lowest temperature = ' + str(lowest))
		print('Average = ' + str(average))
		print(str(cold_day) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

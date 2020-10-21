"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


def main():
	"""
	TODO: make a weather analyzer
	enter temperature and end by entering -100
	sense and print the highest as well as the lowest temperature among all temperature entered
	count and print the amount of day which has a temperature below 16 degree
	calculate and print the average temperature
	"""
	print('weather master Peter 4.0')
	sum_temp = 0
	sum_n = 0
	high_temp = 0
	low_temp = 100
	cold_days = 0
	while True:
		Temp = float(input("please enter temperature:(enter -100 to exit) "))
		if Temp != -100:
			sum_temp = sum_temp + Temp
			sum_n = sum_n + 1
			if high_temp < Temp:
				high_temp = Temp
			if low_temp > Temp:
				low_temp = Temp
			if Temp < 16:
				cold_days = cold_days + 1
		else:
			temp_avg = sum_temp / sum_n
			print('highest: ' + str(float(high_temp)))
			print("lowest: " + str(float(low_temp)))
			print('average: ' + str(float(temp_avg)))
			print(str(int(cold_days)) + "cold day(s)")



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()

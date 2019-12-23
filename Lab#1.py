import math
import random

number_list = [1,2,3,4,5,6,7,8,9,10]

print("Input a number between 1 - 10")

number1 = input("1st number = ")
number2 = input("2nd number = ")


x = 100000
while True:
	if number1 == random.choice(number_list) > x:
		print(number1)
		x += 1
	else:
		print("-Counting is over-")



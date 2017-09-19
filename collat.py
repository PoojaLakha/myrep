import sys

def collatz(number):

	if number == 1 or number == 0:
		sys.exit()

	if number % 2 == 0:
		value = number // 2
		print(value)
	elif number % 2 == 1:
		value = 3 * number + 1
		print(value)

	if not value == 1:
		collatz(value)
	else:
		sys.exit()

print("Enter number:")
num = input()
collatz(int(num))
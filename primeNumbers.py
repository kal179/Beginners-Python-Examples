# Prime number Determiner
# replace input() with raw_input() in Python version 2.7 input() works with version 3

def isPrime(a):
	# If num is prime, returns the given number.
	# If num is not prime, returns the first number it is divisible by.
	if a > 2:
		for x in list(range(2,int(a/2)+1)):
			if a % x == 0:
				return x
				break
		return a
	else:
		return a

while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd.upper().strip() == 'START':
		toCheckNum = int(input('Number to check: '))
		a = isPrime(toCheckNum)
		if a == toCheckNum:
			print(str(toCheckNum) + ' is a prime number.')
			continue
		else:
			print(str(toCheckNum) + ' is divisible by ' + str(a) + '.')
			print(str(toCheckNum) + ' is not a prime number.')
			continue
	else :
		print('Program Ended...')
		break

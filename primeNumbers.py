# Prime number Determiner
# replace input() with raw_input() in Python version 2.7 input() works with version 3 

while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd == 'Start':
		toCheckNum = int(input('Number to Check : '))
		if toCheckNum > 1:
			for x in range(2, toCheckNum):
				if toCheckNum % x == 0:
					print(str(toCheckNum) + ' is divisible by ' + str(x))
					print(str(toCheckNum) + ' is not a Prime number')
					break
				elif toCheckNum % x > 0:
					print(str(toCheckNum) + ' is a prime number')
					break
			continue				
		else :
			print(str(toCheckNum) + ' is not a prime number')
			continue					
	else : 
		print('Progarm Ended...')
		break		



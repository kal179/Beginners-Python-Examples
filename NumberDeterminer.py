# Determines weather the number is positive negative or zero
# If you want to run this code in Python 3 version replace raw_input() with input()

print('Hello,')
while True:
	startorEnd = str(raw_input('Start or End : '))
	print(' ')
	if startorEnd.strip() == 'Start':
		userGet = float(raw_input('Number : '))
		print(' ')
		if userGet > 0 :
			print('Positive')
			print(' ')
		elif userGet == 0 :
			print('Zero')
			print(' ')
		elif userGet < 0 :
			print('Negative')
			print(' ')
		continue	
	elif startorEnd.strip() == 'End':		
		print('Program Ended...')
		break

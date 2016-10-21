# ASCII value of a character
while True:
	getPlain = str(input('Character : '))
	if len(getPlain) == 1:
		print('ASCII value is ',ord(getPlain))
		break
	else:
		print('Entered value is a string and not a character')	
		continue
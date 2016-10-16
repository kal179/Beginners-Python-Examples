# function to sort strings
def sortString():
	strr = str(input('Enter : '))
	words = strr.split()
	words.sort()
	print(' ')
	for word in words:
		print(word)

# main code
print('Hello,')
while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd == 'Start':
		print(' ')
		print(sortString())	
		continue
	elif startOrEnd == 'End' :
		print(' ')
		quit()	# closes interpreter 
	else :
		print('Oops Try Again')
		continue		
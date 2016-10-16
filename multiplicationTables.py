# Multiplication Table viewer

while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd == 'Start':
		whichTable = int(input('Which Table : '))
		for x in range(1, 13):
			table =  whichTable * x
			print(table)
		continue
	else :
		print('Program Ended...')
		break	

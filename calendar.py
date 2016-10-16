# calender viewer
import calendar

# unction to view calendar
def viewCalender():
	yy = int(input('Year : '))
	mm = int(input('Month : '))
	view = calendar.month(yy , mm)
	print('\n' + view)

# main user interaction code
print('Hello,')
while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd == 'Start':
		print(' ')
		print(viewCalender())	
		continue
	elif startOrEnd == 'End' :
		print(' ')
		quit()	# closes interpreter you can import sys to access quit() or dont change it'll work without importing
	else :
		print('Oops Try Again')
		continue
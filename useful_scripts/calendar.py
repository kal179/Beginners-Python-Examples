# calender viewer
import calendar
import sys

# function to view calendar
def viewCalender(yy, mm):
	# Void Function
	print('\n\n Calendar > \n' + calendar.month(yy , mm) + "\n")

# UI
while True:
	if str(input("[+] Start [Y/n] ?  ")).strip().lower() == "y":
		viewCalender(int(input('\nYear : ')), int(input('Month : ')))
	else:
		print("\nSee Ya Soon!")
		sys.exit(0)
		

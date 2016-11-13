# Timer in python (Console Application)
import time
import webbrowser

def timer(minutes):
	a = 0
	while a != minutes: 
		time.sleep(60)
		a = a + 1
	print("<<<<<<Timed out>>>>>>")	
	# I have not used return cause it termites the function
	webbrowser.open_new("https://www.youtube.com/watch?v=SlZMVAydqaE")
	

print("Hello,")
while True:
	start_or_end = str(input("Start or End : "))
	if start_or_end.strip() == "Start":
		get_minutes = int(input("Minutes : "))
		print(timer(get_minutes))
		continue
	else:
		break 

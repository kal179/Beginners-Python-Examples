def twelve_to_twenty_four():
	time = input().strip()
	if (time[-2:] == 'PM'):
		if (time[:2] == "12"):  return(time[:-2])
		else:  return(str(12 + int(time[:2])) + time[2:-2])
	else:
		if (time[:2] == "12"):  print("00" + time[2:-2])
		else:  return(time[:-2])    
		
# Input Format : 12:00:00AM / 03:12:00PM		
print(twelve_to_twenty_four())		
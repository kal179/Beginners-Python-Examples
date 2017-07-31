# Determines weather the number is positive negative or zero
# If you want to run this code in Python 3 version replace raw_input() with input()
def pos_neg_zero(x):
	if x < 0:
		return "Negative"
	elif x > 0:
		return "Positive"
	return "Zero"

print('Hello,')
while True:
	start_or_end = str(raw_input('Start or End : ')).strip().lower()
	if start_or_end == 'start':
		print(pos_neg_zero(float(raw_input('Number: '))), "\n")
		continue	
	else:
		break

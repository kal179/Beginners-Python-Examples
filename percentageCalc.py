# Percentage Calculator
def percentToOrig():
	whatPercent = float(input('What Percent : '))
	ofWhat = float(input('Of What Percent : '))
	orignal = whatPercent / 100 * ofWhat
	print(orignal)

print(percentToOrig())	
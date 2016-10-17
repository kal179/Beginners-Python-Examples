# BMI calculator
# BMI = weight / height * height

while True:
	startOrEnd = str(input('Count or End : '))
	if startOrEnd == 'Count':
		convFact = 0.45
		convFactor = 0.025
		getWeight = float(input('Weight in Pounds : '))
		getHeight = float(input('Height in Inches : '))
		weightInKG = getWeight * convFact
		heightInM = (getHeight * convFactor) * (getHeight * convFactor)
		bmIndex = weightInKG / heightInM
		print('\nHealthy BMI ranges between 19 to 25')
		if 18 < bmIndex < 26 :
			print('Your BMI is ' + str(bmIndex))
			print('You are HEALTHY\n')
		else : 
			print('Your BMI is ' + str(bmIndex))
			print('Your BodyMassIndex isn\'t between Healthy range\n')
		continue	
	else :
		quit()
					 
# BMI calculator
# BMI = weight(kg) / height ** 2(m) standard metrics

def body_mass_index(weight, height):
	return round((weight) / ((height  * 0.01) ** 2), 2)

while True:
	startOrEnd = str(input('Count or End : ')).strip()
	if startOrEnd.lower() == 'count':
		index = body_mass_index(float(input('Weight in Kg : ')), float(input('Height in Centimetre : ')))
		print('\nHealthy BMI ranges between 19 to 25:')
		if 18 < index < 26 :
			print('Your BMI is ' + str(index) + '\nYou are HEALTHY\n')
		else : 
			print('Your BMI is ' + str(index) + '\nYour BodyMassIndex isn\'t between Healthy range\n')
		continue	
	else :
		quit()
	 

def complementary():
	while(True):	
		complementary = float(input('Complementary of : '))
		if complementary <= 90:
			complement = 90 - complementary
			return(complement)
			break
		else:
			print('Number greater than 90 degree. Try again')
			continue

def supplementary():
	while(True):	
		supplementary = float(input('Supplementary of : '))
		if supplementary <= 180:
			supplement = 180 - supplementary
			return(supplement)
			break
		else:
			print('Number greater than 180 degree. Try again')
			continue		

while(True):
	countOrEnd = str(input('Count or End : '))
	if countOrEnd.strip() == 'Count':
		print('\nSupp for supplementary\nComp for complementary')
		getSuppOrCom = str(input('Supp or Comp : '))
		if getSuppOrCom.strip() == 'Supp':
			print(supplementary())
			continue
		elif getSuppOrCom.strip() == 'Comp':
			print(complementary())
			continue
		else:
			break
	else:
		quit()			

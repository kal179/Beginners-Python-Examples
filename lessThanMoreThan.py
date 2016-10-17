nums = [12,34,65,43,21,97,13,57,10,32]
finalNums = []
moreFinalNums = []

def compareMore(a):
	for x in nums:
		if x > a :
			c = finalNums.append(x)

def compareLess(d):
	for x in nums:
		if x < d :
			c = moreFinalNums.append(x)
		
get = int(input('To Compare More Than : '))
getAgain = int(input('To Compare Less Than : '))

print('\nMore Than Values : ')
print(compareMore(get))
print(finalNums , '\n')

print('\nLess Than Values : ')
print(compareLess(getAgain))
print(moreFinalNums,'\n')

			
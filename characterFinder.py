# Number of Character in String Counter

def countVowels(unknownC,unknownT):
	count = 0
	for x in unknownT :
		if x == unknownC:
			count = count + 1
	print('Number of Characters are : ' + str(count))

getText = str(input('Text : '))
print(' ')
getChar = str(input('Which Char To Find : '))
print(' ')
print(countVowels(getChar,getText))

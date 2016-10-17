# Pig Latin Word Altering Game
# function to convert word in pig latin form
def alterWords():
	wordToAlter = str(input('Word To Translate : '))
	alteredWord = wordToAlter[1:] + wordToAlter[0:2] + 'y' # translating word to pig latin
	if len(wordToAlter) < 46 :
		print(alteredWord)
	else :
		print('Too Big . Biggest Word in English Contains 45 characters.')

# main interaction code 
while True:
	startOrEnd = str(input('Start or End : '))
	if startOrEnd == 'Start':
		print(' ')
		print(alterWords())
		continue
	else :
		quit()			 
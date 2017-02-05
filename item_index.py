"""Algorithm for finding index of element in an array"""

def index(array, item):
	index = 0
	found = False
	while (not found):
		if (array[index] == item):
			found = True
		else:
			index = index + 1
	return index 

print index([12, 34], 34)	
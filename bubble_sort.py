
def bubble_sort(array):
	"""Bubble Sort Elem Swapping algorithm"""
	for i in range(len(array)):
		for i in range(len(array) - 1):
			a = array[i]
			b = array[i + 1]
			if (b < a):
				array[i + 1] = array[i]
				array[i] = b 
	return array

a = [3,56,32,65,43,2]
print bubble_sort(a)	
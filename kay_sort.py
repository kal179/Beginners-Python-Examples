"""
This sort is same as reverse sort by me.
Except minor changes in first for loop, and
comparison sign on line 11
And function is called kay_sort because
kay is my nickname
"""

def kay_sort(array):
	print "Orignal List : {}".format(array)
	for i in range(len(array)):
		for n in range(len(array) - 1):
			a = array[n]
			if (a > array[i]):
				tem = array[i]
				array[i] = a 
				array[n] = tem 
	return "Sorted List : {}".format(array)			
	
print kay_sort([123, 4, 123, 4])	

"""
This sort is same as reverse sort by me.
Except minor changes in first for loop, and
comparison sign on line 11
And function is called kay_sort because
kay is my nickname
"""

def kay_sort(array):
	for i in range(len(array)):
		for n in range(len(array) - 1):
			a = array[n]
			if (a > array[i]):
				tem = array[i]
				array[i] = a 
				array[n] = tem 
	return array			
	
print reverse_sort([123, 3455, 6577, 546, 345, 22, 56, 7])	
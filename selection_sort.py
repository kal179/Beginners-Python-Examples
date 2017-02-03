"""
My Modified Solution to Selection Sort Algorithm
instead of swapping elem it is appended to another
temporary array. This makes algotrihm less complicated.
"""

def selection_sort(array):
	temp_num = len(array)
	temp_arr = []
	while (len(temp_arr) != temp_num):
		a = min(array)
		temp_arr.append(a)
		del array[array.index(a)]
	
	array = temp_arr
	del temp_arr
	return array	

nums = [4, 12, 9, 2, 5, 6, 8]	
print selection_sort(nums)	

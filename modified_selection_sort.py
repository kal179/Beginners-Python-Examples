"""
My Modified Solution to Selection Sort Algorithm,
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
	return temp_arr

# Test
test_case = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]	
print("By Builtin method: {}".format(sorted(test_case)))
print("By SelectionSort method: {}".format(selection_sort(test_case)))

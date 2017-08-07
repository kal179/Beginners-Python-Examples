from datetime import datetime


# Don't confuse this is "Main" algorithm
# Time calculated is near accurate because of some extra instructions 
# before actually executing the algorithm
def count_cpu_microtime(func_name, *args):
	tmp = [i for i in args]
	t1 = datetime.now().microsecond
	func_name(*tmp)
	time_took = datetime.now().microsecond - t1
	return round(time_took, 5)
	

# Testing

# "Test" algorithm
def binary_search(array, n):
	arr = sorted(array)
	to_return = False 
	first_elem = 0
	last_elem = len(arr) - 1
	while (first_elem <= last_elem):
		mid = (first_elem + last_elem) // 2
		if (arr[mid] == n):
			to_return = True
			break
		else:
			if (n > arr[mid]):
				first_elem = mid + 1
			else:
				last_elem = mid - 1
	return to_return	

result = count_cpu_microtime(binary_search, [12,324,23,213,3,2,1], 1)
print(str(result) + " microsecs")

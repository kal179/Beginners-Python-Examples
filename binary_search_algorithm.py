

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

nums = [0,23,54,5,32,78]	
print binary_search(nums, 32)	
print binary_search(nums, 5)	

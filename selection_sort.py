#Selection Sort
def selection_sort(l):
	# Scan slices l[0:len(l)], l[1:len(l)], …
	for start in range(len(l)):
	# Find minimum value in slice . . .
		minpos = start
		for i in range(start,len(l)):
			if l[i] < l[minpos]:
				minpos = i
				# . . . and move it to start of slice
		(l[start],l[minpos]) = (l[minpos],l[start])
	return(l)	
		
# Test
result = selection_sort([9,8,7,6,5,4,3,2,1])
print("Builtin Method Result: {}".format(sorted([9,8,7,6,5,4,3,2,1])))
print("Selection Sort Method Result: {}".format(result))

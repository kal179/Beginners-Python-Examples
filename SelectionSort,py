#Selection Sort
def SelectionSort(l):
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
		

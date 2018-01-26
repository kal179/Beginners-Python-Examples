#!/usr/bin/python
# -*- coding: utf-8 -*-

# Bubble Sort
# Ideal sorting algorithm for 
# small data/array

# temporary parameter tells
# function to sort a copy of 
# orignal array, and not the array itself

def sort_(arr, temporary = False):
	
	# Making copy of array if temporary is true
	if temporary:
		ar = arr[:]
	else:
		ar = arr
	
	# To blend every element in correct position
	# length of total array is required
	length = len(ar)
	
	# After each iteration right-most
	# element is completed sorted
	while length > 0:

		# So every next time we iterate only
		# through un-sorted elements
		for i in range(0, length - 1):

			# Swapping greater elements to right
			# and smaller to left
			if ar[i] > ar[i+1]:
				tmp = ar[i]
				ar[i] = ar[i + 1]
				ar[i + 1] = tmp

		# making sure loop breaks
		length = length - 1 
	
	# if temporary, then returning
	# copied arr's sorted form
	# cuz if not returned, then function
	# is literally of no use
	if temporary:
		return ar 	

# See proper explaination 
# at: https://www.geeksforgeeks.org/bubble-sort/
# a good site!


# Testing
tests = [[9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [1312, 1110, 98, 76, 54, 32, 10], ] # Add your test cases 
for test in tests:
	c = sort_(test, True) 
	if c == sorted(test):
		print("Orignal: {}".format(test))
		print("Sorted: {}".format(c))
		print("It worked!\n")
	else:
		print("Something went wrong!\n")


# Seems our bubble sort works
# however for small data or array!

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Sudo ALgorithm:
# both functions work on same principle
# Iterate through array/arguments
# add each element to variable(res)
# return sum

def sum_(*args):
	res = 0
	for arg in args:
		res += arg
	return res

def sum_ar(ar, end_i):
	# end_i is the last index of array
	# till which function should add
	# array's elements
	if end_i > 0 and end_i <= len(ar):
		if end_i == len(ar):
			end_i = end_i - 1
	else:
		end_i = len(ar) - 1

	res = 0
	for elem in ar[:end_i + 1]:
		res += elem 

	return res 

# Simple Algorithm

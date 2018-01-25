#!/usr/bin/python
# -*- coding: <encoding name> -*-

from random import randint as r_int 

# generates a random number
# in inclusive list from 0 to 10
n = r_int(0, 10) 
print("Hint: number is between 0 to 10 including 0 and 10\n")


while True:
	usr = int(raw_input("Guess a number: "))
   
	# Make sure user got the hint
	if usr <= 10 and usr >= 0:

		# if correct
		if usr == n:
			print("That's a correct guess!\nYou got it!\n")
			break

		# brings user closer to answer
		elif usr < n:
			print("Try a bigger num!")
		else:
			print("Try a smaller num!")

	else:
		print("Pls read the hint!")
	
	# Continue till guess does not match 'n'
	# the random number
	print("")
	continue

# Is an infinite loop if usr keeps guessing wrong


# Exhaustive numeration (iteration)
# Simple implementation of logarithmic function
# I love math!

# log(b, x) <=> b ** y = x
# So we have to find y!

# Don't use it for decimal numbers
# log(1000) or log(e, x) is not automatically avaliable
def logarithm_integer(b, x):
	if (b > 0 and b != 1) and x > 0:
		for i in range(x):
			if b ** i == x:
				return i 
		return -1
	else:
		return "Invalid input for logarithm"

# Test
print("log(6, 216) -> " + str(logarithm_integer(6, 216)))
print("log(5, 625) -> " + str(logarithm_integer(5, 25)))
print("log(4, 16) -> " + str(logarithm_integer(4, 16)))
print("log(2, 8) -> " + str(logarithm_integer(2, 8)))
print("log(3, 6) -> " + str(logarithm_integer(3, 6)))
print("log(0, 16) -> " + str(logarithm_integer(0, 16)))

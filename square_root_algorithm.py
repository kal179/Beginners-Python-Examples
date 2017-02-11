"""	Function uses prime factorisation method 
	to find square root of number	"""

def prime_factors(c):
	pos = 2
	factors = []
	while (pos <= c):
		if (c % pos == 0):
			c = c // pos
			factors.append(pos)
			continue
		else:
			pos = pos + 1
	return factors

def extract_common(li):
	final = []
	if (len(li) % 2 != 0):
		return "Number is not perfect root."
	else:
		pre = len(li) - 1
		for n in range(0, pre, 2):
			a = li[n]
			b = li[n + 1]
			if (a == b):
				final.append(b)
			else:	
				return "Number is not perfect root."
	return final 

def square_root(take_in):
	res = 1
	for c in take_in:
		res *= c 
	return res 

get_num = int(raw_input("\nNumber : "))	
print square_root(extract_common(prime_factors(get_num))), " "
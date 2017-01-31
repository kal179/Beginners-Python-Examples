

def compare_two(m,n):
	final = []
	for i in range(len(m)):
		if (m[i] > n[i]):
			final.append(m[i])
		else:
			final.append(n[i])
	return final 

a = [12, 24, 36]		
b = [3, 554, 676]
		
print compare_two(a, b)		
				

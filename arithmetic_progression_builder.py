
def sum_sequence(seq):
	# Sn = n / 2 * (t1 + tn) formula from algebra
	t1 = seq[0]
	tn = seq[-1]
	d = seq[1] - seq[0]
	n = len(seq)
	return n / 2 * (t1 + tn)

def build_arithmetic_seq(start, end, diff):
	a_seq = [start]
	try:
		for i in range(start, end):
			a_seq.append(a_seq[-1] + diff)
	except TypeError as typerr:
		print(typerr)
	except Exception as e:
		print(e)
	else:
		return a_seq

# Test 
res = build_arithmetic_seq(1, 10, 2)
print("Arithmetic sequence:")
for _ in res:
	print("  " + str(_))
print("Sum of sequence: {}".format(sum_sequence(res)))

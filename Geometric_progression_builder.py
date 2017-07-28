"""
Simply it just builds a geometric progression on given conditions.
Iterates through t1 till n 
multiplies last values in list to constant
appende it back to list 
COOL!
"""

def build_geo_sequence(start, end, constant):
	hold = [start]
	try:
		for i in range(start, end):
			hold.append(hold[-1] * constant)
	except TypeError as te:
		print(te)
	except Exception as e:
		print(e)
	else:
		return hold

# Test 
res = build_geo_sequence(1, 10, 3)
print("Geo Sequence:")
for i in res:
	print("  " + str(i))
# Expected -> 1, 3, 9, 27, 81, ....
# Here a = 1, d = 3

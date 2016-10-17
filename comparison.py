# Comparison is necessary 

a = [1,2,4,5,6]  # you can add more elements or delete but both lists or 
b = [3,8,1,0,9]  # how many lists you want should contain same number of elements
c = []

for x in range(len(a)):
 	e = a[x]
 	p = b[x]
 	if e > p:
 		c.append(e)
 	else :
 		c.append(p)	

print(c)

# If you know about my Sorting algorithms add this to that program if you want 		
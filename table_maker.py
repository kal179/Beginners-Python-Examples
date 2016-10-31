# Tables maker
num = int(input("Number to make table : "))
li_a = [num for num in range(0 , num * 11 , num)]
 
for digit in li_a:
	print(digit)

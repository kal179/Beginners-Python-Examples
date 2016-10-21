a = [12,43,567,76,978,65,564,65,786,56,54,43,56,87,54,43]
b = [2,345,45,76,67,9876,879,87,65,65,53,34,324,342,432,51]

diffValue = int(input('Difference to find : '))

def findDifference(x , y , diff):
	for i in range(len(x)):
		first = x[i]
		second = y[i]
		if abs(first - second) == diff:
			return(first,second)
		else :
			continue

print(findDifference(a,b,diffValue))				
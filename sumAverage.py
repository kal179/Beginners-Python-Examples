# average of sum of lists
m = [1,43,656,8,54,,908,4,5,23,78,,435,89,45,476,89]
n = [234,56,90,,675,56,786,90,564,8,657,87,64,354,2,75]
q = [34,76,76,564,34,32,16,67,25,98,90,345,235,64,134,76]

def avgSums():
	summingUp = sum(m) + sum(n) + sum(q)
	summed = summingUp / 3
	return(summed)

print(avgSums)	
liOfNums = [52345,746587,98589,54398,9348,45887,49856,9348758,58797]

def sumUp(li):
    summed = 0
    for x in li:
        summed = summed + x
    return(summed)

print(sumUp(liOfNums))

# or a simple way of doing the same thing
'''
def sumUp(li):
    summed = [li]
    for x in summed:
        s = sum(x)
    return(s)

print(sumUp(liOfNums))

in this method you can add more than one lists
'''

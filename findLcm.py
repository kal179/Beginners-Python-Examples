# function to find lcm of two numbers
def findLcm(i,v):
    if i > v:
        x = i
    else:
        x = v
    while True:
        if (x % i == 0) and (x % v == 0):
            lcm = x
            return(x)
            break
        x = x + 1

# Main code
while(True):
    startOrEnd = str(input('Count lcm or End : '))
    if startOrEnd == 'Count lcm':
        getFirst = float(input('First num : '))
        getSecond = float(input('Second num : '))
        print(findLcm(getFirst , getSecond))
    else:
        quit()

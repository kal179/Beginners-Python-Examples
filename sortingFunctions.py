# functions to sort out data
# they act on lists
# you can apply these functions in your programs

# this function takes first and second element from list and compare them
def bubbleSort(g): # g argument is for list
    for x in range(len(g) - 2):
	    a = g[x]
	    b = g[x + 1 + 1]
	    if a > b :
		    return(a)
	    else :
		    return(b)
# use this to convert output into list
# result = list(map(bubbleSort , g)) replace g with parameter

# this function checks even num
def oddSort(odd):# odd can be list or variable
    for x in odd:
        if x % 3 == 0:
    return(x)
# use this to get list as output
# result = list(filter(oddSort , odd)) replace odd with parameter

# this function checks even num
def evenSort(eve):# eve can be list or variable
    for a in eve:
        if a % 2 == 0:
    return(a)
# use this to get list as output
# result = list(filter(evenSort , eve)) replace eve with parameter

# this function checks divisibility
def divisibleSort(divi , get):# here divi is list and get is an variable set to integer or float
    for r in divi:
        if r % get == 0:
    return(r)
# use this to get output
# result = list(filter(divisibleSort , divi , get)) replace arguments with suitable parameters

# this function checks if addition of group of two elements has desired answer
def addBubbleSort(f,user):# here f is list and user is integer or float
    for x in range(len(f) - 2):
        a = f[x]
        b = f[x + 1 + 1]
        if a + b == user:
            return(a,b)
# i havent checked this function check for bugs
# this is how it works
# res = list(filter(addBubbleSort , f , user)) replace arguments with suitable parameters

# this function checks if subtraction of group of two elements has desired answer
def subBubbleSort(z,userSub):
    for x in range(len(z) - 2):
        a = z[x]
        b = z[x + 1 + 1]
        if a - b == useSubr:
            return(a,b)
# i havent checked this function check for bugs
#res = list(filter(subBubbleSort , z , userSub)) replace arguments with suitable parameters

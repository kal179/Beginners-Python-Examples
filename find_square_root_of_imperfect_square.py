# Here I've implemented a method of finding square root of imperfect square 
# Steps (Pseudocode): visit http://burningmath.blogspot.in/2013/12/finding-square-roots-of-numbers-that.html
# Read the steps carefully or you'll not understand the program!

# To check is number is a perfect square or not
def is_perfect_square(n):
    if isinstance(n, float):
        return (False, None)
    for i in range(n + 1):
        if i * i == n:
            return (True, i)
    return (False, None)

# Average 
def average(*args):
    hold = list(args)
    return sum(hold) / len(hold)

# Method  
# Just implementation of steps on above webpage
def sqrt_of_imperfect_square(a, certainty = 6):
    is_square = is_perfect_square(a)
    if is_square[0]:
        return "{} is a perfect square .It's root is {}.".format(a, is_square[1])
    else:
        a = int(a)
        tmp = None
        s1 = max([float(x * x) for x in range(0,a)])
        while True:
            s2 = a / s1
            tmp = average(s1, s2)
            if not(round(tmp * tmp, certainty) == float(a)):
                s1 = tmp
                continue
            else:
            	return tmp
        return -1  # This condition will normally never occur
        
# Test
case = 2613
res = sqrt_of_imperfect_square(case, 9)
print("Test case: " + str(case))
print("Root: " + str(res))
print("Root Squared: " + str(res * res))

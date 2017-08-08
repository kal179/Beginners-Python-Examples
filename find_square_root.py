
# This method is called exhaustive numeration!
# I am checking every possible value
# that can be root of given x systematically
# Kinda brute forcing

def find_square_root(x):
    if type(x) == str:
        return "Expected an integer! Cannot find square root of an string!"
    for i in range(x):
        if i ** 2 == x:
            return i 
    return "{} is not a perfect square".format(x)
    
# Test 
x = 2
result = find_square_root(x)
print("Square root of {} is {}".format(x, result))

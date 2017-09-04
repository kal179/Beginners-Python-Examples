# Find the nearest root and its square

def nearest_square(n):
    i = 0
    found = False
    while (not found):
        if i ** 2 <= n < ((i + 1) ** 2):
            found = True
        else:
            i += 1
    return (i, i ** 2)
    
# Test
case = 40
res = nearest_square(case)
print("Nearest square to {}: \n{}".format(case, res[1]))

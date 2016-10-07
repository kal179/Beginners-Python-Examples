def numbers(*args):
    total = 1
    for x in args:
        total = total * x
    print(total)

numbers(12, 13, 34, 4576, 234536, 2341)    

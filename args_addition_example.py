def addNumbers(*args):
    finalValue = 0
    for i in args:
        finalValue = finalValue + i
    return(finalValue)

print(addNumbers(123,435,876,12,54,76,78954,89,87,56,78,98,56,32,87))

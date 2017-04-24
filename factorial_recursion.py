def factorial(n):

    if (n <= 1):
        return 1

    else:
        res = n * factorial(n - 1)
        return res

print(factorial(input("Number PLease : ")))

#IN collatz sequence you perform few mathematical operation depending on whether a number is even or odd , no matter what the integer is eventually you will get 1.

#operation performed is the number is even = number // 2 and if the number is odd = number * 3 + 1

#example if the number is 5 , out put is 5 16 8 4 2 1
from sys import exit            # really no need to do that but as a precaution is good

def collatz(num):                             # defining the function
    if (num % 2 == 0):
        res = num //2

    elif (num % 2 != 0):
        res = num * 3 + 1
        
    else:
        return 'Enter a valid integer'

    while (res == 1):                          #we need to exit the function after 1 is obtained
        print(res)
        exit(0)

    while (res != 1):
        print(res)
        num = res
        collatz(num)                          #the function should be executing until 1 is obtained


num = int(input('Enter an integer: '))           #asking for input and then calling the function also change input to raw_input in python 2x versions

print("\nReaching one here....")
collatz(num)

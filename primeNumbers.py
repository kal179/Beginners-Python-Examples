# Prime number Determiner
# replace input() with raw_input() in Python version 2.7 input() works with version 3 
import math as Math

POSITIVE_MESSAGE = " is a prime number"
NEGATIVE_MESSAGE = " is not a prime number"


def is_number_prime(number):
    upper_lim = Math.floor(Math.sqrt(number)) + 1
    is_prime = True if number != 1 else False

    for i in range(2, upper_lim):
        if number % i == 0:
            is_prime = False
            break

    return is_prime


while True:
    startOrEnd = str(input('Start or End : '))
    if startOrEnd == 'Start':
        number = int(input('Number to Check : '))
        result = str(number)
        prime_status = is_number_prime(number)

        if prime_status:
            result += POSITIVE_MESSAGE
        else:
            result += NEGATIVE_MESSAGE
        print(result)
    else:
        print('Program Ended...')
        break

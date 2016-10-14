import math
# function to calculate geometricMean mean of two numbers
# pre code
def geometricMean():
    gOne = int(input('First num : '))
    gTwo = int(input('Second num : '))
    gMult = (gOne * gTwo)
    gMean = math.sqrt(gMult)
    print('The geometric Mean of ' + str(gOne) + ' and ' + str(gTwo) + ' is ' + str(gMean))

# main code
# to make this code work in python 3.5 convert raw_input() to str(input())
print("Hello,")
while True:
    startOrEnd = raw_input('Start or End : ')
    if startOrEnd.strip() == 'Start':
        print('Okay let\'s get started \n')
        print(geometricMean())
        continue
    elif startOrEnd.strip() == 'End':
        print('\n Program ended...')
        break
    else :
        print('\n Invalid Input try again')
        continue

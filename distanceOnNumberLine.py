# this is a simple geometric distance formula
# d(x,y) = |x-y| = distance
# where x and y are co-ordinates on a number line

def distance(x,y):
    dist = abs(x-y)
    return(dist)

print('Hello\n')
while(True):
    print('Enter end if you wish to end the program.')
    valueX = input('Value for x co-ordinate : ')
    if valueX == 'end':
        quit()
    valueY = input('Value for y co-ordinate : ')
    print(distance(float(valueX),float(valueY)))
    continue

import math
# Basic Circle

def diameter(radii): # d = 2r r is radius
    diaOfCircle = 2 * radii
    return('Diameter is : ' + str(diaOfCircle))

def circumference(rad): # C = 2pir
    peri = 2 * math.pi * rad
    return('Circumference is : ' + str(peri))

def area(rad): # area = pi r square
    area = math.pi * rad ** 2
    return('Area is : ' + str(area))

#  main
print('Hello\n')
print('Press Enter to exit')
print('=' * 5 + 'Started' + '=' * 5 )
while True:
    user = str(input('Diameter or Circum or Area : '))
    if user == 'Diameter':
        radius = float(input('Radius : '))
        print(diameter(radius))
        continue
    elif user == 'Circum':
        radius = float(input('Radius : '))
        print(circumference(radius))
        continue
    elif user == 'Area':
        radius = float(input('Radius : '))
        print(area(radius))
        continue
    else:
        print('\nProgram Ended...')
        print('=' * 17)
        break

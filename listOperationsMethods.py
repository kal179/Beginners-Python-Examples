# list operations part 2

siliconValley = ['Google','Apple','Dropbox','Facebook','Cisco','Adobe','Oracle','Samsung']
print(siliconValley)

# hmm seems like i forgot to add Electronic Arts in the list siliconValley
# This will add the element at the end of the list
siliconValley.append('Electronic Arts')
print(siliconValley)

# thats cool but I want my element at specific position
siliconValley.insert(5, 'AMD')
# 5 is the position and whatever you add after comma is element

# Okay enough I want to pop out an element from list and I want to use it in a string
# you have to provide the index of elementyou want to pop out
poppedElement = siliconValley.pop(4)
print('Popped element is ' + poppedElement)

# Oops I Samsung isnt in silicon valley, I have to remove Samsung from list
# How am I gonna do thats
# You have to enter the element in parenthesis and not it's index
siliconValley.remove('Samsung')
print(siliconValley)

# I want to sort the list in alphabetical order
# How to do thats
# simple
siliconValley.sort()
# or
sorted(siliconValley)
print(siliconValley)

# I wanted list in reverse alphabetical order
# simple
siliconValley.sort(reverse = True)
# or
sorted(siliconValley , reverse = True) # seperate the reverse with comma
print(siliconValley)

# Okay what if i dont know about the index of an element but i want to print only that element
googleIndex = siliconValley.index('Google')
print(siliconValley[googleIndex])

# I am tired of watching those elements again and again
# How I am going to do thats
# easy
del siliconValley
print(siliconValley) # this should probably give you an NameError

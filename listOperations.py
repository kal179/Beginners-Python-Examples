# list operations
# You can create a list by putting elements inside square brackets[]
# lists are capable of containing any type of data

# a list can contain datas of different datatypes
numsAndAlphas = ['a',1,'hello',3.14159265359,'are you okay',True,'good',False]
# this is going to work
print(numsAndAlphas)

# list accessing
# You can access single items from the list similar to string indexing
# if you dont know string indexing look for my program called stringOperations.py
print(numsAndAlphas[0])
print(numsAndAlphas[1:5])
print(numsAndAlphas[0:])
print(numsAndAlphas[:6])
print(numsAndAlphas[:])
print(numsAndAlphas[2:7:2])
print(numsAndAlphas[::3])

# you can add lists too...
list2 = [2,9,16,25,36,49,64,81,100,144]
newList = numsAndAlphas + list2

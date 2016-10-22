# Checking is some keyword is a python keyword or not
import keyword

pythonKeywords = keyword.kwlist
getToCheck = str(input('Keyword to check : '))
check = keyword.iskeyword(getToCheck)
if check == True:
    print(getToCheck + ' is a python keyword.')
else:
    print(getToCheck + ' is not a python keyword.')

print('\nShowing all keywords in python : \n')
print(pythonKeywords)
# remember to test the code

string = str(input("Enter Text : "))

list_of_ascii = []
for character in string:
	code = ord(character)
	list_of_ascii.append(code)
	
new_string = ""

for element in list_of_ascii:
	new_string = new_string + " " +str(element)
	
print(" ")	
print(new_string)

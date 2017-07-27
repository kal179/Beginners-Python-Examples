# ASCII value of a character
def get_ascii(S):
	if len(S) == 1:
		return 'ASCII value of {} is {} '.format(S, ord(S))
	else:
		return 'Entered value is a string and not a character'
# test
character = 'Z'
character1 = 'z'
print(get_ascii(character))
print(get_ascii(character1))
print(get_ascii("STack"))

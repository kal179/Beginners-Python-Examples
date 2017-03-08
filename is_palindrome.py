

class Palindrome:

	@classmethod
	def is_palindrome(cls, word):
		if (len(word) > 0):
			pre = word[::-1].lower()
			if (pre == word.lower()):
				return True 
			else:
				return False 
		else:
			return None 
			
# Testing the function

get_word = str(input("Enter a Word : "))
print(" ")
print(Palindrome.is_palindrome(get_word))			
		


def is_palindrome(string):
     reversed_word = string[::-1]
     if string == reversed_word:
         return True
     else:
         return False
print(is_palindrome("abccba"))         

#################    OR   ###################

 def is_palindrome(string):
     if string == string[::-1]:
         return True   
     return False
 print(is_palindrome("abccba"))    

#################    OR   ###################


 def is_palindrome(string):
     return string == string[::-1]

 print(is_palindrome("abccba")) 

'''An anagram is a word or phrase created by rearranging the letters of another word or phrase.
For example, the word "heart" can be rearranged to form the word "earth". 
So, "heart" and "earth" are anagrams of each other.'''

def check_anagram(str1,str2):
     # Remove all spaces from both the strings
     # and convert them to lowercase
    str1 = str1.replace(" ","").lower()
    str2 =str2.replace(" ","").lower()
    # if the length of both strings are not equal then return false
    if len(str1) != len(str2):
        return False
    count1 = {}
    count2 = {}
    for i in range(len(str1)):
        count1[str1[i]] = 1+count1.get(str1[i],0)
        count2[str2[i]] = 1+count2.get(str2[i],0)
    for c in count1:
        if count1[c] != count2.get(c,0):
            return False
str1 = input()
str2 = input()
if check_anagram(str1,str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are anagrams")
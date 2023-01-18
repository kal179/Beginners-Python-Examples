# printing hello world is a tradition in beginners 
# it is normally used to if check everything is okay
import sys

#type 1 sys.stdout.write()
sys.stdout.write("Hello, ")
sys.stdout.write("World!")
sys.stdout.write("\n")

#type 2 print()
print("Hello, World!")

#type 3 - format()

word1 = "Hello"
word2 = "World"
print("{} {}".format(word1, word2))

#type 4 - f-strings
word1 = "Hello"
word2 = "World"
print(f"{word1} {word2} ")


#type 5 - join
characters = ['H','e','l','l','o',' ','W','o','r','l','d']
message = "".join(characters)
print(message)

#type 6 - Dict
words = {"Eng_greeting": "Hello", "Eng_world": "World"}
message = " ".join(words.values())
print(message)



# pre code
import random

# func for telling answer and asking question
def magic():
    userQuesInput = input("Ask me a question . Try me: ")
    return random.choice([ "It is certain" , "Outlook good" , "You may rely on it" , "Ask again later" , "Concentrate and ask again" , "Reply hazy, try again" , "My reply is no" , "My sources say no" ])

# main Sector
print("Hello,")
while True:
    # getting started
    user  = input("Start or End: ").strip()
    if user == "Start":
        print(magic(), "\n")
        continue
    elif user == "End":
        print("Program ended...")
        break
    else :
        print("Invalid Input.Try again.")
        continue

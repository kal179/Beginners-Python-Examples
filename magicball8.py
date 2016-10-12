# pre code
import random

# response list
response = [ "It is certain" , "Outlook good" , "You may rely on it" , "Ask again later" ,
 "Concentrate and ask again" , "Reply hazy, try again" , "My reply is no" , "My sources say no" ]

# func for telling answer and asking question
def magic():
    print(" ")
    userQuesInput = raw_input("Ask me a question . Try me : ")
    print(" ")
    forAns = random.choice(response)
    print(forAns)

# main Sector
while True:
    print("Hello,")
    # getting started
    user  = raw_input("Start or End : ")
    if user.strip() == "Start":
        print(" ")
        print(magic())
    elif user.strip() == "End":
        print(" ")
        print("Program ended...")
        break
    else :
        print(" ")
        print("Invalid Input.Try again.")
        continue

    # starting again
    startAgain = raw_input("Start again or End : ")
    if startAgain.strip() == "Start again":
        print("Starting again...")
        print(" ")
        continue
    elif startAgain.strip() == "End":
        print("Program Ended...")
        print(" ")
        break

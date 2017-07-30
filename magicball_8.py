import random

# func for telling answer and asking question
def magic():
    userQuesInput = input("Ask me a question . Try me: ")
    return random.choice([ "It is certain" , "Outlook good" , "You may rely on it" , "Ask again later" , "Concentrate and ask again" , "Reply hazy, try again" , "My reply is no" , "My sources say no" ])

# main Sector
print("Hello,")
while True:
    if input("Start or End: ").strip().lower() == "start":
        print(magic(), "\n")
        continue
    else:
        quit()

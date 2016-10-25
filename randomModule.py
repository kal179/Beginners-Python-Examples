import random


inside = random.randint(1,37890) # choses a random integer between given range
print(inside)

outside = random.randrange(1,1000) # choses a random number number in given range
print(outside)

colors = ['green','black','blue','yellow','white'] 
print(random.choice(colors))  # choses random element from list

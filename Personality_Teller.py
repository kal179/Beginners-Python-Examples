# Personality Teller
import random

personalities = ['Arrogant and Rude','Funny and Polite','Insane and Crazy'
,'Lover and Cute','Nerd and Boring','Cool and Rude','Cute but arrogant','Intelligent and Geek'
,'Cool and Funny','Idiot and Crazy','Awesome and Crazy','Good and Smart','Cool and Smart',
'Smart and Geek','Cool and Smart']

def teller(li):
    name = str(input('Tell Your Name : '))
    randPersonality = random.choice(li)
    return('According to your name You are ' + str(randPersonality) + '.')

print(teller(personalities))

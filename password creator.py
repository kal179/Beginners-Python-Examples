import random
import string

allChars = [ string.ascii_letters + string.digits + string.punctuation ]

password = random.choice(allChars) + random.choice(allChars) + random.choice(allChars) + random.choice(allChars)  + random.choice(allChars) + random.choice(allChars) + random.choice(allChars) + random.choice(allChars)
print(password)

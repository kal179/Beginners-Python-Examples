import random

# "The something in something" program
noun_lib = ["cat","dog","lizard","bald","insane guy","CEO","monkey","teacher","ballerina","old man","nerd","lion","alien"]
place_lib = ["in Hungary","in the toilet","in a car","in a zoo","in a lions cave","in a park","in Norway","in Rio","on Mars","on a tree","on the roof of Burj-Khalifa"]

frame = "The" + " " + random.choice(noun_lib) + " " + random.choice(place_lib) + "."
print(frame)
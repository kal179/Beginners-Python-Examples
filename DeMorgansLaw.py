# Morgans Formula In Algebra Set operations
# number(set A) + number(set B) - number(set A interaction B)
# n(a)+ n(b) - n(anb)
# you can add sets or increase the number elements of sets The formula still works

a = { 1 , 23 , 55 , 76 , 13 , 90 , 34 , 78 }
b = { 12 , 345 , 8 , 4 , 0 , 7 , 4 , 3 , 53 , 4 , 6 , 3 }

abInteraction = a & b      # & operator interacts two sets
abUnion = a | b    # | operator makes union of two sets

eqn = len(a) + len(b) - len(abInteraction)
print(str(eqn) + ' = ' + str(len(abUnion)))

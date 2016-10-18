import random
import turtle
t = turtle.Pen()

for i in range(150):
    t.color(random.choice(['green','red','violet']))
    t.width(5)
    t.forward(i)
    t.right(30)

import turtle

def square():
    win = turtle.Screen()
    win.bgcolor("white")
    jack = turtle.Turtle()
    for x in range(1,5):
              jack.forward(100)
              jack.right(90)
    win.exitonclick()
       
square()      

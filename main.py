import turtle
import random
ex = turtle.Turtle()
s = turtle.Screen()
turtle.colormode(255)

c = []
for i in range(255):
    c.append(i)


d = [0,90,180,270]
ex.speed("fastest")
ex.pensize(1)
ex.penup()
ex.setx(-250)
ex.sety(-200)
ex.pendown()
for i in range(10):
    
    for x in range(10):
        color = (random.choice(c),random.choice(c),random.choice(c))
        
        #ex.pendown()
        ex.dot(20, color)
        #ex.penup()
        ex.forward(50)
    ex.left(90)
    ex.forward(50)
    ex.right(90)
    ex.backward(500)
s.exitonclick()
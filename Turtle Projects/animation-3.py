import turtle
turtle.bgcolor("red")
t = turtle.Turtle()
t.speed(-3)
for i in range(100):
    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(50)
    t.right(30)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.left(360/100)
turtle.mainloop()

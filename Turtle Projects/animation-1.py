import turtle
turtle.bgcolor("black")
turtle.title("Animation Circle")
t = turtle.Turtle()
t.color("red")
t.speed(0)
t.hideturtle()
for i in range(100):
    t.circle(i*2)
    t.left(5)
turtle.mainloop()


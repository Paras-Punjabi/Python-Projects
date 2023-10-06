import turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.up()
t.goto((-50,0))
t.down()
number = 100
t.color("red")
for i in range(number):
    for j in range(4):
       t.forward(200)
       t.left(90)
    t.left(360/number)
t.hideturtle()
turtle.mainloop()
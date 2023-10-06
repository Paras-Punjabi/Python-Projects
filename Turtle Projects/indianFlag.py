import turtle,math
t =turtle.Turtle()
t.hideturtle()
turtle.title("Indian Flag")
t.speed(0)
t.up()
t.goto((-200,-280))
t.down()
t.showturtle()

t.left(90)
t.forward(550)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)

t.color("green")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.end_fill()

t.color("black")
t.left(90)
t.forward(100)

t.color("orange")
t.begin_fill()
t.left(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.end_fill()

t.up()
t.color("blue")
t.hideturtle()
t.right(90)
t.forward(200)
t.showturtle()
t.down()
t.circle(50)

t.up()
t.hideturtle()
t.left(90)
t.forward(50)
t.showturtle()
t.down()

t.left(90)

t.pensize(2)
for i in [k*15 for k in range(0,32)]:
    x = 50*math.sin(i)
    y = 50*math.cos(i)
    t.goto((x,y+120))
    t.goto((0,120))

t.goto((0,110))
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()
    
t.up()
t.goto((-50,-200))
t.write("😎😎😎😎😎😎😎😎",font=("monospace",30,"bold"))





turtle.mainloop()
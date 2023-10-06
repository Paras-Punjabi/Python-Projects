import turtle,math
turtle.title("Happy Rakshabandhan")
turtle.screensize(canvwidth=400,canvheight=400,bg="ghost white")
t = turtle.Turtle()
t.pensize(10)
t.speed(10)

t.up()
t.goto((-300,-300))
t.down()
t.goto((-77,-77))
t.up()
t.goto((0,-100))
t.down()

t.up()
t.goto((77,77))
t.down()
t.goto((300,300))

k = 0
for i in [k*20 for k in range(0,11)]:
    t.up()
    t.home()
    x = 100*math.cos(i)
    y = 100*math.sin(i)
    t.goto((x,y))
    t.down()
    if k%2==0:
        t.color("orange")
    else:
        t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    k +=1

t.up()
t.goto((0,-80))
t.down()
t.color("black","orangered")
t.begin_fill()
t.circle(100)
t.end_fill()

t.up()
t.goto((0,0))
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()
for i in [k*20 for k in range(0,11)]:
    t.up()
    x = 60*math.cos(i)
    y = 60*math.sin(i)
    t.goto((x,y+14))
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(5)
    t.end_fill()

t.up()
t.goto((-370,250))
t.down()
t.write("Happy Rakshabandhan Disha Bua❤❤❤",font=("monospace",25,"bold"))
t.hideturtle()

turtle.mainloop()



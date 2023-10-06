import turtle
from math import sin , cos 

if __name__ == '__main__':
    t = turtle.Turtle()
    turtle.title("Captain America Shield")
    # t.speed(0)
    t.up()
    t.hideturtle()
    t.goto((0,-200))
    t.down()
    t.showturtle()

    t.color("red")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

    t.color("white")
    t.up()
    t.goto((0,-160))
    t.down()
    t.begin_fill()
    t.circle(160)
    t.end_fill()

    t.color("red")
    t.up()
    t.goto((0,-110))
    t.down()
    t.begin_fill()
    t.circle(110)
    t.end_fill()

    t.color("blue")
    t.up()
    t.goto((0,-80))
    t.down()
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    t.up()
    t.home()
    t.down()
    t.color("white")
    t.up()

    t.goto((80*cos(162),80*sin(162)))
    t.down()
    t.left(120)
    t.begin_fill()
    
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()

    t.up()
    t.goto((-180,250))
    t.down()
    t.color("black")
    t.write("CAPTAIN AMERICA",font=("monospace",30,"bold"))
    t.hideturtle()
    turtle.mainloop()
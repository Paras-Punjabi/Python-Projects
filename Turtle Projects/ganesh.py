import turtle
turtle.title("Ganesh Chaturthi")
t = turtle.Turtle()
turtle.Screen().bgcolor("#FCE02C")

def goto(x,y):
    t.up()
    t.goto((x,y))
    t.down()

def toHome():
    t.up()
    t.home()
    t.down()

if __name__ == '__main__':
    t.pencolor("#920C0C")
    t.speed(0)
    t.pensize(5)
    t.shape("turtle")

    goto(-30,200)
    t.color("#920C0C")

    # tilak - triangle
    t.begin_fill()
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.end_fill()

    # tilak-Wave - 1
    goto(-40,180)
    t.left(120)
    t.circle(150,5)
    t.pensize(8)
    t.circle(150,10)
    t.pensize(5)
    t.circle(150,5)

    # tilak-Wave - 2
    toHome()
    goto(-40,165)
    t.circle(200,5)
    t.pensize(8)
    t.circle(200,10)
    t.pensize(5)
    t.circle(200,5)

    # tilak-Wave - 3
    toHome()
    goto(-40,150)
    t.circle(230,5)
    t.pensize(8)
    t.circle(230,10)
    t.pensize(5)
    t.circle(230,5)

    # trunk
    goto(38.66,153.87)
    t.right(90)
    for i in range(60):
        if(i > 50):
            t.right(2)
        else:
            t.right(1)
        t.forward(3)
    
    for i in range(40):
        if i > 20:
            t.left(3)
            t.pensize(t.width()-0.2)
        else:
            t.left(1.5)
        t.forward(3)
    
    # right ear
    t.pensize(5)
    toHome()
    goto(58.66,153.87)
    t.left(30)
    for i in range(7):
        t.circle(-40,20)
        t.pensize(t.width() + 0.42)
    t.right(30)
    for i in range(70):
        t.pensize(t.width() - 0.1)
        t.forward(1)

    # right leg
    toHome()
    goto(45,-1.55)
    for i in range(30):
        t.forward(1)
        t.pensize(t.width()+0.1)
    t.pensize(6)
    t.circle(-60,140)

    t.pensize(5)
    t.right(20)
    for i in range(200):
        t.pensize(t.width()+0.01)
        if i > 100 and i < 150:
            t.left(0.2)
        t.forward(1)
    
    t.circle(40,120)
    for i in range(40):
        t.pensize(t.width()-0.05)
        t.circle(40,1)
    

    # left-leg
    toHome()
    goto(-42.40,-141.72)
    t.left(170)
    for i in range(200):
        t.circle(-200,0.25)
        t.pensize(t.width() + 0.02)
    t.pensize(5)
    for i in range(200):
        t.circle(-60,1)
        t.pensize(t.width() + 0.02)
    
    for i in range(50):
        t.forward(1)
        t.right(1)
        t.pensize(t.width()-0.1)

    # left-hand
    toHome()
    t.pensize(5)
    goto(-101.96,112.64)
    t.left(220)
    t.forward(30)
    toHome()
    goto(-101.96,112.64)
    t.right(110)
    for i in range(30):
        t.forward(1)
        t.pensize(t.width() + 0.1)
    
    t.circle(-30,120)
    t.right(30)
    t.forward(20)
    for i in range(40):
        t.forward(1)
        t.right(1)
        t.pensize(t.width() - 0.1)
    t.pensize(8)
    t.circle(-30,120)


    # left-ear
    t.pensize(5)
    toHome()
    goto(-71.96,72.64)
    t.left(100)
    for i in range(50):
        t.pensize(t.width()+0.1)
        if i>5:
            t.left(0.5)
        t.forward(2)

    for i in range(10):
        t.pensize(t.width()-0.5)
        t.right(3)
        t.forward(2)
    t.pensize(6)
    t.circle(-30,200)

    for i in range(10):
        t.right(10)
        t.pensize(t.width()-0.2)
        t.forward(3)
    
    # eyelashes
    toHome()
    goto(-45.73,119.09)
    t.pensize(1)
    t.right(20)
    for i in range(22):
        t.pensize(t.width()+0.1)
        t.left(2)
        t.forward(1)

    for i in range(23):
        t.pensize(t.width()+0.2)
        t.right(3)
        t.forward(1)
    

    # eyes
    toHome()
    t.pensize(2)
    goto(-4,105.71)
    t.left(160)
    for i in range(23):
        t.pensize(t.width() + 0.12)
        t.left(1)
        t.forward(1)

    for i in range(23):
        if i > 15:
            t.forward(2)
            t.right(2)
        else:
            t.pensize(t.width() - 0.08)
            t.left(2)
            t.forward(1)
    
    for i in range(5):
        t.right(1)
        t.forward(1)
    
    t.right(220)

    for i in range(20):
        t.left(1)
        t.forward(2)

    for i in range(20):
        t.left(3.5)
        t.forward(1)
    
    t.forward(10)
    
    goto(-15.13,93.18)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    goto(-350,250)
    t.write("Happy Ganesh Chaturthi😊😊😊😊",font=("Courier",30,"bold"))

    t.hideturtle()
    turtle.mainloop()
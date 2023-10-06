import turtle,math
from pygame import mixer

# utility functions
def goto(x,y):
    t.up()
    t.goto((x,y))
    t.down()

if __name__ == '__main__':
    turtle.Screen().bgcolor("#140A0B")
    turtle.title("Shang-Chi: The Lord Of Ten Rings")
    turtle.screensize(canvwidth=400,canvheight=400)
    t = turtle.Turtle()

    # loading marvel music
    mixer.init()
    mixer.music.load("./marvel.mp3")

    t.speed(2)
    t.pensize(10)
    t.pencolor("#BA0218")

    length = 150 # radius of bigger circle
    radius = 60 # radius for small circle

    # play marvel music
    mixer.music.play()

    # code for making ten rings
    for i in range(1,11):
        x = length*math.sin(1.8*i*math.asin(radius*math.sqrt(3)/(2*length)))
        y = length*math.cos(1.8*i*math.asin(radius*math.sqrt(3)/(2*length)))
        goto(x,y)
        t.circle(radius)
        goto(0,0)
    
    goto(-370,-240)
    t.write("Shang-Chi The Lord Of Ten Rings".upper(),font=("monospace",30,"bold"))
    t.hideturtle()

    turtle.mainloop()
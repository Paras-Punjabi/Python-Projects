import turtle,random
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red","yellow","blue","green","violet","pink","purple"]
radius = 10
for i in range(120):
    t.color(colors[random.randint(0,len(colors)-1)])
    t.circle(radius,45)
    radius +=2
turtle.mainloop()
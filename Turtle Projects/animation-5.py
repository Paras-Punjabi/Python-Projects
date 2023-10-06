import turtle
def Spiral (python , cplusplus):
    if python >0:
        turtle.forward(python)
        turtle.right(cplusplus)
        Spiral(python-5,cplusplus)
turtle.shape("classic")
turtle.reset()
turtle.pen(speed =1)
turtle.delay(0)
length =400
turn_by =121
turtle.penup()
turtle.setpos(-length/2,length/2)
turtle.pendown()
Spiral(length,turn_by)
   
turtle.mainloop()
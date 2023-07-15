from pygame import Rect,draw
from random import sample
from constants import WIDTH,HEIGHT,BLOCK_SIZE,xArray,yArray

class Food:
    def __init__(self,x,y,width,height):
        self.position = {'x':x,'y':y}
        self.width = width
        self.height = height
        self.color = (255,0,0)
    
    def getRandomPosition(self,snake):
        x = sample(xArray,1)[0]
        y = sample(yArray,1)[0]
        self.position = {'x':x,'y':y}

    
    def draw(self,window):
        draw.rect(window,self.color,Rect(self.position['x'],self.position['y'],self.width,self.height))

from pygame import Rect,draw
from constants import WIDTH,HEIGHT,BLOCK_SIZE

class Snake:
    def __init__(self,x,y,width,height) -> None:
        self.position = {'x':x,'y':y}
        self.width = width
        self.height = height
        self.color = (0,255,0)
        self.score = 0
        self.snake_array = [self.position]
        self.direction = {'x':1,'y':0}
    
    def goLeft(self):
        if(self.direction['x'] == 1):
            return
        self.direction = {'x':-1,'y':0}
    
    def goRight(self):
        if(self.direction['x'] == -1):
            return
        self.direction = {'x':1,'y':0}
    
    def goUp(self):
        if(self.direction['y'] == 1):
            return
        self.direction = {'x':0,'y':-1}
    
    def goDown(self):
        if(self.direction['y'] == -1):
            return
        self.direction = {'x':0,'y':1}
    
    def checkCollision(self)->bool:
        x = self.position['x']
        y = self.position['y']
        if(x<0 or x > WIDTH or y < 0 or y>=HEIGHT):
            return True
        return False

    def increaseLength(self):
        last = self.snake_array[len(self.snake_array)-1]
        self.snake_array.append({'x':last['x'],'y':last['y']})
    
    def moveSnake(self):
        for i in range(len(self.snake_array)-1,0,-1):
            self.snake_array[i]['x'] = self.snake_array[i-1]['x']
            self.snake_array[i]['y'] = self.snake_array[i-1]['y']
        
        self.snake_array[0]['x'] += self.direction['x']*BLOCK_SIZE
        self.snake_array[0]['y'] += self.direction['y']*BLOCK_SIZE
    
    def checkEatFood(self,food) -> None:
        food_x = food.position['x']
        food_y = food.position['y']
        x = self.position['x']
        y = self.position['y']
        if(x==food_x and y == food_y):
            food.getRandomPosition(self)
            self.score+=5
            self.increaseLength()
    
    def collisionWithItself(self) -> bool:
        for i in range(1,len(self.snake_array)):
            if(self.position['x'] == self.snake_array[i]['x'] and self.position['y'] == self.snake_array[i]['y']):
                return True
        return False

    def draw(self,window):
        item = self.snake_array[0]
        draw.rect(window,(246,190,0),Rect(item['x'],item['y'],self.width,self.height))
        for i in range(1,len(self.snake_array)):
            item = self.snake_array[i]
            draw.rect(window,self.color,Rect(item['x'],item['y'],self.width,self.height))
        
        
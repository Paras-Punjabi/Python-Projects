import pygame
from food import Food
from snake import Snake
from constants import *
import os

class Game:
    def __init__(self):   
        pygame.init()
        self.snakeSpeed = BLOCK_SIZE/FRAME_RATE
        self.display = pygame.display
        self.display.set_icon(pygame.image.load("./icon.png"))
        self.window = self.display.set_mode((WIDTH,HEIGHT+BLOCK_SIZE)) # surface of game
        self.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        pygame.font.init()
        self.score = pygame.font.Font('freesansbold.ttf', BLOCK_SIZE-2)
        
        self.snake:Snake = Snake(4*BLOCK_SIZE,6*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)
        
        self.food:Food = Food(10*BLOCK_SIZE,10*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE)

        self.game_over:bool = False
    
    def storeHighScore(self):
        if(not os.path.exists("./highscore.txt")):
            f = open("highscore.txt",'w')
            f.write(str(self.snake.score))
            return self.snake.score
        
        f = open("highscore.txt",'r')
        s = f.read()
        if(s == ""):
            s = 0
        s = max(int(s),self.snake.score)
        f = open("./highscore.txt",'w')
        f.write(str(s))
        return s    
        
    
    def makeBackground(self):
        light = (0,100,0)
        dark = (1,46,31)
        for i in range(0,int(WIDTH/BLOCK_SIZE)):
            for j in range(0,int(HEIGHT/BLOCK_SIZE)):
                if (i+j)%2==0:
                    pygame.draw.rect(self.window,light,pygame.Rect(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))
                else:
                    pygame.draw.rect(self.window,dark,pygame.Rect(i*BLOCK_SIZE,j*BLOCK_SIZE,BLOCK_SIZE,BLOCK_SIZE))

    def run(self):
        once = True
        hs = 0
        while not self.game_over:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    self.game_over = True
                
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_UP:
                        self.snake.goUp()
                    if events.key == pygame.K_DOWN:
                        self.snake.goDown()
                    if events.key == pygame.K_RIGHT:
                        self.snake.goRight()
                    if events.key == pygame.K_LEFT:
                        self.snake.goLeft()
            self.snake.moveSnake()
                
            if(self.snake.checkCollision() or self.snake.collisionWithItself()):
                self.snake.direction = {'x':0,'y':0}
                if once:
                    hs = self.storeHighScore()
                    once = False
                
                self.window.fill((255,255,255))
                font = pygame.font.Font('freesansbold.ttf', 2*BLOCK_SIZE)
                f = font.render(f"Game Over!",False,(0, 0, 0))
                self.window.blit(f,(WIDTH/2-5.5*BLOCK_SIZE,HEIGHT/4))

                f = self.score.render(f"Score: {self.snake.score}",False,(0,0,0))
                self.window.blit(f,(WIDTH/2-2*BLOCK_SIZE,HEIGHT/2))

                f = self.score.render(f"High Score: {hs}",False,(0,0,0))
                self.window.blit(f,(WIDTH/2-3*BLOCK_SIZE,2*HEIGHT/3))

                self.display.update()
                continue
            
            self.window.fill((255,255,255))
            self.snake.checkEatFood(self.food)
            self.makeBackground()
            self.snake.draw(self.window)
            self.food.draw(self.window)

            font = self.score.render(f"Score: {self.snake.score}",False,(0, 0, 0))
            self.window.blit(font,(WIDTH/2-2*BLOCK_SIZE,HEIGHT))

            self.display.update()
            self.clock.tick(FRAME_RATE)
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

    
    

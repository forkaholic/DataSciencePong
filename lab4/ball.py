import pygame
import numpy as np


class Ball:
    # pass
    #class variables
    RADIUS = 10

    
    def __init__(self, x,y, vx,vy, screen, fgcolor, bgcolor, CONSTS):
        #instance variables
        self.x = x
        self.y = y
        self.screen = screen
        self.vx = vx
        self.vy = vy
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS
        
    def show(self, color):
        #Rect:left/top, width/height
        pygame.draw.circle(self.screen, color, (self.x, self.y), Ball.RADIUS)
        
    def reset(self):
        #reset ball/paddle to center
        self.show(self.bgcolor)
        self.x = self.CONSTS.WIDTH - Ball.RADIUS - self.CONSTS.BORDER
        self.y = self.CONSTS.HEIGHT // 2
        self.vx = -self.CONSTS.VELOCITY #np.random.randint(-VELOCITY, 0) #-VELOCITY
        self.vy = np.random.randint(-self.CONSTS.VELOCITY, self.CONSTS.VELOCITY+1)
        self.update()
        # print("reseted")
        
    def update(self, paddle=0):
        #np = op + dp
        #delete the old ball
        self.show(self.bgcolor)
        #
        newx = self.x + self.vx
        newy = self.y + self.vy
        # self.show(self.fgcolor)
        # print(self.CONSTS.BORDER)

        #Check if I'm collliding (wall position):
            # flip the velocity

        #Left wall:
        if newx < (self.CONSTS.BORDER+self.RADIUS):
            self.vx = - self.vx
        #Bottom / Top wall
        elif newy > (self.CONSTS.HEIGHT-self.CONSTS.BORDER-self.RADIUS) or newy < (self.CONSTS.BORDER+self.RADIUS):
            self.vy = -self.vy

        #paddle bounce
        if paddle != 0:
            #ballx behind the paddle
            px = self.CONSTS.WIDTH-self.RADIUS - self.CONSTS.BORDER
            #bally over paddle
            py1 = paddle.y-paddle.L//2 #p0 top
            py0 = paddle.y+paddle.L//2 #p0 bottom
            if newx > px and (newy > py1 and newy < py0):
                self.vx = - self.vx
            #edge bounce
            elif newx > px and (newy == py1 or newy == py0):
                self.vx = - self.vx
                self.vy = np.random.randint(-self.CONSTS.VELOCITY, self.CONSTS.VELOCITY+1)


        self.x = self.x + self.vx
        self.y = self.y + self.vy
        # self.show(self.fgcolor)
        self.show(pygame.Color("yellow"))

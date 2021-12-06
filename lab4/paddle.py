import pygame
from pygame import color

class Paddle:
    # pass

    #paddle constants:
    L = 80 #length
    STEP = 20 #move size

    def __init__(self, y, screen, fgcolor, bgcolor, CONSTS):
        self.y = y
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS
        self.W = CONSTS.BORDER #width


    def show(self, color):
        # pass
    # Rect(left, top, width, height) -> Rect
    # update top, based on y:
        top = self.y-Paddle.L//2
        pygame.draw.rect(self.screen, color, pygame.Rect( (self.CONSTS.WIDTH-self.W, top),(self.W, Paddle.L)))

    def update(self, dir):
        #delete old paddle
        self.show(self.bgcolor)
        if dir < 0 and self.y > self.CONSTS.BORDER+Paddle.L//2: #up
            self.y -= Paddle.STEP
        elif dir > 0 and self.y < self.CONSTS.HEIGHT-self.CONSTS.BORDER-Paddle.L//2: #down
            self.y += Paddle.STEP
        # else: #nothing
        #     self.y = self.y
        self.show(self.fgcolor)

    def reset(self):
        self.show(self.bgcolor)
        self.y = self.CONSTS.HEIGHT // 2
        self.update(0)

#init, show, update
#--init y only
#show: draw rect
#update: clear color, get pos, change color

#update ball to check for bounce. 
#make sure paddle in bounds (y)
# quit 
# if x is below 0. lost. 
# print time
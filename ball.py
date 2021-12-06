import pygame
import numpy as np

class Ball:
    RADIUS = 20
    # DEBUG count = 0
    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor,CONSTS):
        self.x = x
        self.vx = vx
        self.y = y 
        self.vy = vy   
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.CONSTS = CONSTS

    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    # Calculates the new position of the ball based on axis
    # NOTE: This method does not update the velocity of the ball
    def bounce(self, pos, vel, wall):
        if vel < 0:
            # DEBUG print(f"Distance to travel = {vel*fr}\nDistance from wall = {pos - wall}\nRemaining distance = {(pos - wall) - (vel*fr)}")
            return (pos - wall) - (vel * self.CONSTS.FPS) + wall
        elif vel > 0:
            # DEBUG print(f"Distance to travel = {vel*fr}\nDistance from wall = {wall-pos}\nRemaining distance = {(wall - pos) - (vel*fr)}")
            return wall - ((wall - pos) - (vel * self.CONSTS.FPS)) #FINISH HERE AND IN RESPECTIVE SPOT IN UPDATE
        print(f"Error with bounce, Inputs: Pos: {pos}, Wall: {wall}, Framerate: {self.CONSTS.FPS}")
        
    # Updates the position for the ball while redrawing the ball (not updating, pong does that)
    def update(self, paddle=0): 
        # DEBUG self.count = self.count + 1
        # DEBUG print(self.count)
        # DEBUG print(f"X: {self.x}\nVX: {self.vx}\nY: {self.y}\nVY: {self.vy}")
        
        self.show(self.bgcolor)

        # Ball will not end up in a valid position
        if self.x + self.vx <= self.CONSTS.FPS + self.RADIUS:
            self.x = self.bounce(self.x, self.vx, self.CONSTS.BORDER + self.RADIUS)
            self.vx = -self.vx
        else:
            self.x = self.x + self.vx 
        
        # Ball will not end up in a valid position
        newpos = self.y + self.vy
        if newpos <= self.CONSTS.BORDER + self.RADIUS or newpos >= self.CONSTS.HEIGHT - self.CONSTS.BORDER - self.RADIUS:
            # Ball is moving up
            if self.vy < 0:
                # Want ball to bounce when the radius hits the wall, not when the center hits
                self.y = self.bounce(self.y, self.vy, self.CONSTS.BORDER + self.RADIUS)
            # Ball is moving down
            else:
                self.y = self.bounce(self.y, self.vy, self.CONSTS.HEIGHT - self.CONSTS.BORDER - self.RADIUS)
            self.vy = -self.vy
        else:
            self.y = self.y + self.vy

        #paddle bounce
        if paddle != 0:
            #ballx behind the paddle
            px = self.CONSTS.WIDTH-self.RADIUS - self.CONSTS.BORDER
            #bally over paddle
            py1 = paddle.y-paddle.L//2 #p0 top
            py0 = paddle.y+paddle.L//2 #p0 bottom
            if self.x > px and (self.y > py1 and self.y < py0):
                self.vx = - self.vx
            #edge bounce
            elif self.x > px and (self.y == py1 or self.y == py0):
                self.vx = - self.vx
                self.vy = np.random.randint(-self.CONSTS.VELOCITY, self.CONSTS.VELOCITY+1)

        # DEBUG print(f"X: {self.x}\nVX: {self.vx}\nY: {self.y}\nVY: {self.vy}")        
        self.show(self.fgcolor)



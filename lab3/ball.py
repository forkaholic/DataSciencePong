import pygame

class Ball:
    RADIUS = 20
    # DEBUG count = 0
    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor):
        self.x = x
        self.vx = vx
        self.y = y 
        self.vy = vy   
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
    
    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    # Calculates the new position of the ball based on axis
    # NOTE: This method does not update the velocity of the ball
    def bounce(self, pos, vel, wall, fr):
        if vel < 0:
            # DEBUG print(f"Distance to travel = {vel*fr}\nDistance from wall = {pos - wall}\nRemaining distance = {(pos - wall) - (vel*fr)}")
            return (pos - wall) - (vel * fr) + wall
        elif vel > 0:
            # DEBUG print(f"Distance to travel = {vel*fr}\nDistance from wall = {wall-pos}\nRemaining distance = {(wall - pos) - (vel*fr)}")
            return wall - ((wall - pos) - (vel * fr)) #FINISH HERE AND IN RESPECTIVE SPOT IN UPDATE
        print(f"Error with bounce, Inputs: Pos: {pos}, Wall: {wall}, Framerate: {fr}")
        
    # Updates the position for the ball while redrawing the ball (not updating, pong does that)
    def update(self, wsize, height, fr): 
        # DEBUG self.count = self.count + 1
        # DEBUG print(self.count)
        # DEBUG print(f"X: {self.x}\nVX: {self.vx}\nY: {self.y}\nVY: {self.vy}")
        
        self.show(self.bgcolor)

        # Ball will not end up in a valid position
        if self.x + self.vx <= wsize + self.RADIUS:
            self.x = self.bounce(self.x, self.vx, wsize + self.RADIUS, fr)
            self.vx = -self.vx
        else:
            self.x = self.x + self.vx 
        
        # Ball will not end up in a valid position
        newpos = self.y + self.vy
        if newpos <= wsize + self.RADIUS or newpos >= height - wsize - self.RADIUS:
            # Ball is moving up
            if self.vy < 0:
                # Want ball to bounce when the radius hits the wall, not when the center hits
                self.y = self.bounce(self.y, self.vy, wsize + self.RADIUS, fr)
            # Ball is moving down
            else:
                self.y = self.bounce(self.y, self.vy, height - wsize - self.RADIUS, fr)
            self.vy = -self.vy
        else:
            self.y = self.y + self.vy
        # DEBUG print(f"X: {self.x}\nVX: {self.vx}\nY: {self.y}\nVY: {self.vy}")        
        self.show(self.fgcolor)



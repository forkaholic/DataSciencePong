from typing import FrozenSet
import pygame
import random
import math

from pygame import math as pgmath
from ball import Ball
from paddle import Paddle
from pygame.constants import QUIT

def main():
    pygame.init()

    WIDTH = 1280
    HEIGHT = 720
    # make velocity scale off of screen size, larger screens feel slow
    # buttery smooth, but is absolutely overkill
    VELOCITY = 15/240 * 30
    FPS = 240
    fgcolor = pygame.Color('white')
    bgcolor = pygame.Color('black')

    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #ball
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    
    angle = (random.random() * 0.5 * math.pi) + (0.75 * math.pi)
    vx0 = math.cos(angle) * VELOCITY
    print("XVEL " + str(vx0))
    vy0 = math.sin(angle) * VELOCITY
    print("YVEL " + str(vy0))

    ball = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor)
    ball.show('white')

    #walls
    wcolor = pygame.Color("grey")
    wsize = 20
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,0), (WIDTH,wsize)))
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,HEIGHT-wsize), (WIDTH,wsize)))
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,0), (wsize,HEIGHT)))
    pygame.display.update()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # put outside for gif creation
        pygame.display.update()
        clock.tick(FPS) 
        ball.update(wsize, HEIGHT, 1/FPS)
            


if __name__ == "__main__":
    main()
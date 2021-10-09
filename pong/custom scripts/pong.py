import pygame
from pygame.constants import QUIT

def main():
    pygame.init()

    WIDTH = 840
    HEIGHT = 680

    pygame.display.set_caption("Lab2")
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #walls
    wcolor = pygame.Color("grey")
    wsize = 20
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,0), (WIDTH,wsize)))
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,HEIGHT-wsize), (WIDTH,wsize)))
    pygame.draw.rect(screen, wcolor,pygame.Rect((0,0), (wsize,HEIGHT)))

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
if __name__ == "__main__":
    main()
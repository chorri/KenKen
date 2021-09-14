import pygame
import pygame_menu
from pygame.locals import *
from Kenken import solve
pygame.init()
surface = pygame.display.set_mode((600, 400))
def set_grid(value, difficulty):
    # Do the job here !
    pass
def solver():
    solve()
def start_the_game():
    # Do the job here !
    img = set_grid
    pygame_menu.events.CLOSE
    pygame.display.set_caption("¡Kenken running!")
    surface = pygame.display.set_mode((750, 800))
    menu = pygame_menu.Menu('Kenken csp solver', 750, 800,
                        theme=pygame_menu.themes.THEME_BLUE)
    
    menu.add.image("kenken_grid.PNG", scale=(0.8, 0.8))
    menu.add.button('Run', solver)
    menu.mainloop(surface)
    
 
pygame.display.set_caption("TA1: Solver para Kenken")
menu = pygame_menu.Menu('Kenken csp solver', 600, 400,
                        theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Select Grid :', [('10x10', 1)], onchange=set_grid)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

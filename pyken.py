import pygame
import pygame_menu
from pygame.locals import *
from Kenken import solve
import sys
# Inicio de pygame
pygame.init()
# Tamaño de la pantalla
surface = pygame.display.set_mode((600, 400))
# Variables globales
RED = (255, 0, 0)
GRAY = (150, 150, 150)
v = -1
# Funcion llamanda desde el atributo selector del pygame_menu
def set_grid(value, difficulty):
    global v
    v = difficulty
    print(v)
# Solver solo llama al algoritmo cps
def solver():
    solve()
def start_the_game():
    # Elegir la grilla
    img_name = "10x10.PNG"
    if v == 1:
        img_name = "10x10.PNG"
    elif v == 2:
        img_name = "9x9.PNG"
    # Cerrar el menu
    pygame_menu.events.EXIT
    # Titulo
    pygame.display.set_caption("CPS")
    # Incrementar tamaño de pantalla
    surface = pygame.display.set_mode((750, 750))
    run = True
    # Cargar imagen del tablero
    tablero = pygame.image.load(img_name).convert()
    rect = tablero.get_rect()
    rect.center = 750//1.5, 750//1.5
    tablero = pygame.transform.scale(tablero, (600, 600))
    font1 = pygame.font.SysFont('ActionIsShaded', 30)
    textsurface = font1.render("hola", False , RED)
    # Bucle para mantener el programa corriendo
    while run:
        for event in pygame.event.get():
            # Si cierran la ventana vuelve al menu
            if event.type == pygame.QUIT:
                run = False
                surface = pygame.display.set_mode((600, 400))
            
        # background color
        surface.fill(GRAY)
        # Dibuja ablero
        surface.blit(tablero, rect)
        surface.blit(textsurface, (80,80))
        pygame.display.update()
    
# Aqui comienza el codigo:
# Configuraciones con pygame_menu
pygame.display.set_caption("TA1: Solver para Kenken")
menu = pygame_menu.Menu('Kenken csp solver', 600, 400, theme=pygame_menu.themes.THEME_BLUE)
# Estos metodos usan un callback para llamar una funcion
menu.add.selector('Select Grid :', [('10x10', 1),('9x9', 2)], onchange=set_grid)
# El importante es este start_game
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
# Loop para que no se cierre el menu
menu.mainloop(surface)
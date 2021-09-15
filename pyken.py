import pygame
import pygame_menu
from Kenken import solve
import sys
# Inicio de pygame
pygame.init()
# Tamaño de la pantalla
surface = pygame.display.set_mode((600, 400))
# Variables globales
RED = (255, 0, 0)
GRAY = (150, 150, 150)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
WHITE = (255,255,255)
# Test Texto
font1 = pygame.font.SysFont('ActionIsShaded', 30)
v = -1
grilla_sol = None
# Funcion llamanda desde el atributo selector del pygame_menu
def set_grid(value, difficulty):
    global v
    v = difficulty
    print(v)
def start_the_game():
    global grilla_sol
    grilla_sol = solve()
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
    #textsurface = font1.render(str(grilla_sol[0][0]), False , RED)
    # Boton run
    x_button = 300
    y_button = 700
    w_button = 80
    h_button = 80
    button = pygame.Rect(x_button, y_button, w_button, h_button)
    active = False
    # Bucle para mantener el programa corriendo
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                surface = pygame.display.set_mode((600, 400))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button.collidepoint(event.pos):
                #print("hola")
                active = True 
        # background color
        surface.fill(GRAY)
        # Dibuja Tablero
        surface.blit(tablero, rect)
        # Dibujar Boton
        pygame.draw.rect(surface, RED, button)
        text_surf = font1.render("Run", True, BLUE)
        text_rect = text_surf.get_rect(center=(x_button + 38, y_button + 22))
        surface.blit(text_surf, text_rect)
        if active:
            y = 110 
            x = 110
            for i in range(10):
                for j in range(10):
                    test_text = font1.render(str(grilla_sol[i][j]), True, RED)
                    surface.blit(test_text, (x,y))
                    x+=58.8
                x=110
                y+=58.6
        pygame.display.update()
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
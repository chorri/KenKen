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
BLUE = (0, 0, 255)
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
    global grilla_sol, v
    grilla_sol = solve(v)
    # Elegir la grilla
    img_name = "sum.PNG"
    if v == 1:
        img_name = "sum.PNG"
    elif v == 2:
        img_name = "mult.png"
    # Cerrar el menu
    pygame_menu.events.EXIT
    # Titulo
    pygame.display.set_caption("CSP")
    # Incrementar tamaño de pantalla
    surface = pygame.display.set_mode((750, 750))
    run = True
    # Cargar imagen del tablero
    tablero = pygame.image.load(img_name).convert()
    rect = tablero.get_rect()
    rect.center = 750//1.5, 750//1.5
    if v == 1:
        rect.center = 750//1.5, 750//1.5
    elif v == 2:
        rect.center = 750//1.6555, 750//1.65
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
# Titulo
pygame.display.set_caption("Solver para resolver el puzzle Kenken")
menu = pygame_menu.Menu('Kenken', 600, 400, theme=pygame_menu.themes.THEME_BLUE)
# Dificultad
menu.add.selector('Selecciona tabla:', [('sumas y restas', 1),('multiplicaciones', 2)], onchange=set_grid)
# Jugar y Salir
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
# Loop para que no se cierre el menu
menu.mainloop(surface)
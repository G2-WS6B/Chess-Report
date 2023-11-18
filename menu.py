import pygame
import sys
from main import main  # Importa la función main desde el archivo main.py

# Configuración de la ventana y colores
pygame.init()
WIDTH = 480
show_difficulty_buttons = False
WIN = pygame.display.set_mode((WIDTH, WIDTH))
width, height = 840, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("G2 Chess")
background_image = pygame.image.load("images/background.png").convert()
background_level = pygame.image.load("images/background_level.png").convert()
background_image = pygame.transform.scale(background_image, (width, height))
font_path = "font/KdamThmorPro-Regular.ttf"
font = pygame.font.Font(font_path, 24)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BEIGE = (246, 231, 216)
MUSTARD = (244, 179, 36)


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def button(msg, x, y, w, h, inactive_color, active_color, action=None):
    global show_difficulty_buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    clicked = False  # Inicializa la variable que registra si se hizo clic

    # Verifica si el cursor está sobre el botón
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))  # Dibuja un rectángulo activo

        # Verifica si se hizo clic y si hay una acción asociada al botón
        if click[0] == 1 and action is not None:
            if action == "play":
                show_difficulty_buttons = True  # Cambia a mostrar botones de dificultad
            elif action == "exit":
                pygame.quit()  # Sale del juego
                sys.exit()
            else:
                clicked = True  # Marca como clickeado

    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))  # Dibuja un rectángulo inactivo

    # Renderiza y muestra el texto en el botón
    text_surf, text_rect = text_objects(msg, font)  # Usa la fuente global
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)

    return clicked  # Devuelve si el botón fue clickeado


depth = -1


def game_menu():
    global show_difficulty_buttons, depth
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Sale del juego
                sys.exit()

        screen.blit(background_image, (0, 0))  # Muestra el fondo de la pantalla

        if not show_difficulty_buttons:  # Si no se muestran los botones de dificultad
            if button("Play", 518, 200, 274, 50, MUSTARD, (0, 200, 0), action="play"):
                show_difficulty_buttons = True  # Activa los botones de dificultad al clickear "Play"
            button("Exit", 518, 280, 274, 50, BEIGE, (200, 0, 0), action="exit")
        else:  # Muestra los botones de dificultad
            screen.blit(background_level, (0, 0)) # Cambia el fondo de la pantalla
            if depth != -1:
                print("Tree depth: ", depth)  # Imprime la profundidad seleccionada
                main(WIN, WIDTH, depth)  # Inicia el juego con la profundidad seleccionada
            if button("Easy", 91, 200, 309, 50, MUSTARD, (0, 200, 0), action="easy"):
                depth = 1  # Establece la profundidad en 1 (Fácil)
            if button("Medium", 91, 260, 309, 50, MUSTARD, (0, 200, 0), action="medium"):
                depth = 2  # Establece la profundidad en 2 (Media)
            if button("Hard", 91, 320, 309, 50, MUSTARD, (0, 200, 0), action="hard"):
                depth = 3  # Establece la profundidad en 3 (Difícil)

        pygame.display.update()  # Actualiza la pantalla


game_menu()  # Ejecuta la función del menú del juego



import pygame
from extras import *
from button import Button
from pantallaNombre import *

def win(screen):
  #sonido menu
  pygame.mixer.music.load("Sonidos/posgameMusica.mp3")
  pygame.mixer.music.play()
  pygame.mixer.music.set_volume(0.1) #configuración del volumen
  
  #sonido botones
  sonidoBotonAdelante = pygame.mixer.Sound("Sonidos/botonAdelante.mp3")
  sonidoBotonAdelante.set_volume(0.2)
    
  while True:
    imagenMenu = pygame.image.load("Imagenes/win.png")
    
    screen.blit(imagenMenu, (0, 0))

    mouse_pos = pygame.mouse.get_pos()
    
    win_texto = letra(35).render("HAZ INGRESADO CON EXITO", True, "White")
    win_pos = win_texto.get_rect(center=(650, 350))
    screen.blit(win_texto, win_pos)
    
    win2_texto = letra(35).render(" TODAS LAS PALABRAS CORRECTAS", True, "White")
    win2_pos = win_texto.get_rect(center=(550, 450))
    screen.blit(win2_texto, win2_pos)
    
    saltar_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(1025, 650), 
                        text_input="SALTAR", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    
    for button in [saltar_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if saltar_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          ingresarNombre(screen)

    pygame.display.update()
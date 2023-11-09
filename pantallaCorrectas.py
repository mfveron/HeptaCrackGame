import pygame
from extras import *
from button import Button
from pantallaHistorial import *
from pantallaNombre import *

def gameOver(screen, acertadas): #crea la pantalla de posjuego donde se muestran las palabras correctas ingresadas, ordenadas alfabeticamente y dibujadas en una determinada posicion
    #sonido menu
    pygame.mixer.music.load("Sonidos/posgameMusica.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1) #configuración del volumen
    
    #sonido botones
    sonidoBotonAdelante = pygame.mixer.Sound("Sonidos/botonAdelante.mp3")
    sonidoBotonAdelante.set_volume(0.2)
    
    while True:
      imagenMenu = pygame.image.load("Imagenes/gameOver.png")
      
      screen.blit(imagenMenu, (0, 0))

      mouse_pos = pygame.mouse.get_pos()
      
      gameOver_texto = letra(35).render("Palabras Correctas Ingresadas:", True, "White")
      gameOver_pos = gameOver_texto.get_rect(center=(640, 250))
      screen.blit(gameOver_texto, gameOver_pos)
      
      saltar_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(1025, 650), 
                          text_input="SALTAR", font=letra(40), base_color="#d7fcd4", hovering_color="White")
      
      for button in [saltar_BUTTON]:
        button.changeColor(mouse_pos)
        button.update(screen)
      
      defaultFont= pygame.font.Font( pygame.font.get_default_font(), 25)
      acertadas.sort() #ordena alfabeticamente
      cont = 0
      for elemento in acertadas:
        cont += 1
        if cont == 1:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 325))
        if cont == 2:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 375))
        if cont == 3:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 425))
        if cont == 4:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 475))
        if cont == 5:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 525))
        if cont == 6:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 575))
        if cont == 7:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (115, 625))
        if cont == 8:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 325))
        if cont == 9:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 375))
        if cont == 10:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 425))
        if cont == 11:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 475))
        if cont == 12:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 525))
        if cont == 13:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 575))
        if cont == 14:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (275, 625))
        if cont == 15:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 325))
        if cont == 16:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 375))
        if cont == 17:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 425))
        if cont == 18:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 475))
        if cont == 19:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 525))
        if cont == 20:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 575))
        if cont == 21:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (435, 625))
        if cont == 22:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 325))
        if cont == 23:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 375))
        if cont == 24:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 425))
        if cont == 25:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 475))
        if cont == 26:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 525))
        if cont == 27:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 575))
        if cont == 28:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (595, 625))
        if cont == 29:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (755, 325))
        if cont == 30:
            ingresadas = defaultFont.render(elemento, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (755, 375))
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if saltar_BUTTON.checkForInput(mouse_pos):
                sonidoBotonAdelante.play()
                ingresarNombre(screen)

      pygame.display.update()
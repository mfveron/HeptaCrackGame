import pygame
from extras import *
from button import *
from funcionesRESUELTO import *

def puntaje(screen): #crea la pantalla de historial que muestra el puntaje y el nombre guardado en el archivo txt previamente
  #sonido botones
  sonidoBotonAdelante = pygame.mixer.Sound("Sonidos/botonAdelante.mp3")
  sonidoBotonAdelante.set_volume(0.2)
  
  while True:
    imagenMenu = pygame.image.load("Imagenes/tablero1.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    gameOver_texto = letra(45).render("TOP 10:", True, "White")
    gameOver_pos = gameOver_texto.get_rect(center=(640, 40))
    screen.blit(gameOver_texto, gameOver_pos)
    
    ranking = []
    puntaje = []
    
    lecHistorialPuntaje(ranking)
  
    for i in range(len(ranking)): 
      if i % 2 == 0:
        puntaje.append(int(ranking[i])) #creamos una lista puntajes y nos aseguramos que los numeros se pasen en formato int
    
    puntaje.sort(reverse=True) #ordenamos la lista puntajes de mayor a menor
    
    for i in range(len(puntaje)): #volvemos a pasar a la lista a str
      puntaje[i] = str(puntaje[i])
    
    
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 50)
    
    
    for i in range(0,len(puntaje)-1): #dibujamos uno por uno el puntaje y su correspondiente nombre en una determinada posición 
      if i == 0:
        screen.blit(defaultFont.render("#1", 1, COLOR_TEXTO), (100, 100))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (250, 100))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (400, 100))
      if i == 1:
        screen.blit(defaultFont.render("#2", 1, COLOR_TEXTO), (100, 200))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (250, 200))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (400, 200))
      if i == 2:
        screen.blit(defaultFont.render("#3", 1, COLOR_TEXTO), (100, 300))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (250, 300))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (400, 300))
      if i == 3:
        screen.blit(defaultFont.render("#4", 1, COLOR_TEXTO), (100, 400))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (250, 400))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (400, 400))
      if i == 4:
        screen.blit(defaultFont.render("#5", 1, COLOR_TEXTO), (100, 500))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (250, 500))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (400, 500))
      if i == 5:
        screen.blit(defaultFont.render("#6", 1, COLOR_TEXTO), (700, 100))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (850,100))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (1000, 100))
      if i == 6:
        screen.blit(defaultFont.render("#7", 1, COLOR_TEXTO), (700, 200))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (850, 200))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (1000, 200))
      if i == 7:
        screen.blit(defaultFont.render("#8", 1, COLOR_TEXTO), (700, 300))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (850, 300))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (1000, 300))
      if i == 8:
        screen.blit(defaultFont.render("#9", 1, COLOR_TEXTO), (700, 400))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (850, 400))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (1000, 400))
      if i == 9:
        screen.blit(defaultFont.render("#10", 1, COLOR_TEXTO), (700, 500))
        screen.blit(defaultFont.render(puntaje[i], 1, COLOR_TEXTO), (850, 500))
        screen.blit(defaultFont.render(ranking[ranking.index(puntaje[i])+1], 1, COLOR_TEXTO), (1000, 500))
      
    menuPrincipal_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(1025, 650), 
                        text_input="MENU", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    
    for button in [menuPrincipal_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
          if menuPrincipal_BUTTON.checkForInput(mouse_pos):
            sonidoBotonAdelante.play()
            from principal import main_menu
            main_menu() #llamamos dentro de la funcion para retornar al main_menu

    pygame.display.update()



import pygame
from extras import *
from funcionesRESUELTO import *
from button import *
from pantallaHistorial import *

def ingresarNombre(screen): #crea la pantalla de posjuego que le pide al usuario que ingrese su nombre para guardarlo en un archivo txt
  #sonido botones
  sonidoBotonAdelante = pygame.mixer.Sound("Sonidos/botonAdelante.mp3")
  sonidoBotonAdelante.set_volume(0.2)
  sonidoTecla = pygame.mixer.Sound("Sonidos/tecla.mp3")
  
  candidataNombre = ""
  dibujarNombre(screen, candidataNombre)
  
  while True:
    
    mouse_pos = pygame.mouse.get_pos() 
  
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
        #Ver si fue apretada alguna tecla
      if event.type == KEYDOWN:
        sonidoTecla.play()
        letraApretada = dameLetraApretada(event.key)
        candidataNombre += letraApretada   #va concatenando las letras que escribe
        if event.key == K_BACKSPACE:
            candidataNombre = candidataNombre[0:len(candidataNombre)-1] #borra la ultima
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        if guardar_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          crearHistorialPuntaje(candidataNombre) #guarda el nombre ingresado en un archivo txt
          puntaje(screen) #llama a la funcion para pasar a la pantalla de Historial
    
    imagenMenu = pygame.image.load("Imagenes/gameOver2.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    dibujarNombre(screen, candidataNombre) #dibuja en pantalla las letras que se van ingresando
    
    ingresarN_texto = letra(45).render("Ingresar Nombre:", True, "White")
    ingresarN_pos = ingresarN_texto.get_rect(center=(640, 150))
    screen.blit(ingresarN_texto, ingresarN_pos)
       
    guardar_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(1025, 650), 
                        text_input="GUARDAR", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    
    for button in [guardar_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
  
    pygame.display.update()
#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from pantallaJuego import *
from extras import *
from button import Button

#Centrar la ventana y despues inicializar pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
#pygame.mixer.init()

#Preparar la ventana
pygame.display.set_caption("HeptaCrack") #titulo de la ventana
screen = pygame.display.set_mode((ANCHO, ALTO))

imagenMenu = pygame.image.load("Imagenes/diseño4.png")

#sonido menu
pygame.mixer.music.load("Sonidos/musicaMenu.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1) #configuración del volumen

#sonido botones
sonidoBotonAdelante = pygame.mixer.Sound("Sonidos/botonAdelante.mp3")
sonidoBotonAtras = pygame.mixer.Sound("Sonidos/botonAtras.mp3")
sonidoBotonAdelante.set_volume(0.2)
sonidoBotonAtras.set_volume(0.3)

#guardamos el tiempo de inicio en una variable
tiempo_inicial = pygame.time.get_ticks()

def libre():
  while True:
    imagenMenu = pygame.image.load("Imagenes/D4.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    dificultad_texto = letra(25).render("SELECCIONE LA EXTENSION MINIMA DE LAS PALABRAS:", True, "White")
    dificultad_pos = dificultad_texto.get_rect(center=(640, 75))
    screen.blit(dificultad_texto, dificultad_pos)

    cuatro_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(350, 250), 
                        text_input="4", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    cinco_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(925, 250), 
                        text_input="5", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    seis_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(350, 450), 
                        text_input="6", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    siete_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(925, 450), 
                        text_input="7", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    atras_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 650), 
                    text_input="VOLVER", font=letra(35), base_color="#d7fcd4", hovering_color="White")
    
    for button in [cuatro_BUTTON, cinco_BUTTON, seis_BUTTON, siete_BUTTON, atras_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if cuatro_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(40,1000), "normal", 4, diferencia_tiempo)
        if cinco_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(40,1000), "normal", 5, diferencia_tiempo)
        if seis_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(40,1000), "normal", 6, diferencia_tiempo)
        if siete_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(40,1000), "normal", 7, diferencia_tiempo)
        if atras_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAtras.play()
          modoDeJuego()

    pygame.display.update()

def tematico():
  while True:
    imagenMenu = pygame.image.load("Imagenes/D4.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    dificultad_texto = letra(35).render("SELECCIONE UNA VERSION:", True, "White")
    dificultad_pos = dificultad_texto.get_rect(center=(640, 75))
    screen.blit(dificultad_texto, dificultad_pos)

    nombres_BUTTON = Button(image=pygame.image.load("Imagenes/extraLargo_borde.png"), pos=(640, 250), 
                        text_input="NOMBRES Y APELLIDOS", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    paises_BUTTON = Button(image=pygame.image.load("Imagenes/extraLargo_borde.png"), pos=(640, 450), 
                        text_input="PAISES Y CIUDADES", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    atras_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 650), 
                    text_input="VOLVER", font=letra(35), base_color="#d7fcd4", hovering_color="White")
    
    for button in [nombres_BUTTON, paises_BUTTON, atras_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if nombres_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(20,1000), "nombres", 3, diferencia_tiempo)
        if paises_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(10,1000), "paises", 3, diferencia_tiempo)
        if atras_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAtras.play()
          modoDeJuego()

    pygame.display.update()

def dificultad():
  while True:
    imagenMenu = pygame.image.load("Imagenes/D4.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    dificultad_texto = letra(35).render("SELECCIONE UNA DIFICULTAD:", True, "White")
    dificultad_pos = dificultad_texto.get_rect(center=(640, 75))
    screen.blit(dificultad_texto, dificultad_pos)

    facil_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(640, 200), 
                        text_input="FACIL", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    normal_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(640, 350), 
                        text_input="NORMAL", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    dificil_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(640, 500), 
                        text_input="DIFICIL", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    atras_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 650), 
                    text_input="VOLVER", font=letra(35), base_color="#d7fcd4", hovering_color="White")
    
    for button in [facil_BUTTON, normal_BUTTON, dificil_BUTTON, atras_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if facil_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(40,1000), "normal", 3, diferencia_tiempo)
        if normal_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(20, 40), "normal", 3, diferencia_tiempo)
        if dificil_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          pygame.mixer.music.stop()
          diferencia_tiempo = pygame.time.get_ticks() - tiempo_inicial
          jugar(screen, range(5,20), "normal", 3, diferencia_tiempo)
        if atras_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAtras.play()
          modoDeJuego()

    pygame.display.update()

def modoDeJuego():
  while True:
    
    imagenMenu = pygame.image.load("Imagenes/D4.png")
    
    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    modo_texto = letra(35).render("SELECCIONE UN MODO DE JUEGO:", True, "White")
    modo_pos = modo_texto.get_rect(center=(640, 75))
    screen.blit(modo_texto, modo_pos)

    normal_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(350, 250), 
                        text_input="NORMAL", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    tematico_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(925, 250), 
                        text_input="TEMATICO", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    libre_BUTTON = Button(image=pygame.image.load("Imagenes/mediano_borde.png"), pos=(640, 450), 
                        text_input="LIBRE", font=letra(40), base_color="#d7fcd4", hovering_color="White")
    atras_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 650), 
                    text_input="VOLVER", font=letra(35), base_color="#d7fcd4", hovering_color="White")
    
    for button in [normal_BUTTON, tematico_BUTTON, libre_BUTTON, atras_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if normal_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          dificultad()
        if tematico_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          tematico()
        if libre_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          libre()
        if atras_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAtras.play()
          main_menu()

    pygame.display.update()
    
def main_menu():
  while True:

    screen.blit(imagenMenu, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()

    jugar_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 350), 
                        text_input="JUGAR", font=letra(50), base_color="#d7fcd4", hovering_color="White")
    historial_BUTTON = Button(image=pygame.image.load("Imagenes/largo_borde.png"), pos=(640, 500), 
                        text_input="HISTORIAL", font=letra(50), base_color="#d7fcd4", hovering_color="White")
    salir_BUTTON = Button(image=pygame.image.load("Imagenes/chico_borde.png"), pos=(640, 650), 
                        text_input="SALIR", font=letra(50), base_color="#d7fcd4", hovering_color="White")

    for button in [jugar_BUTTON, historial_BUTTON, salir_BUTTON]:
      button.changeColor(mouse_pos)
      button.update(screen)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if jugar_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          modoDeJuego()
        if historial_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAdelante.play()
          puntaje(screen)
        if salir_BUTTON.checkForInput(mouse_pos):
          sonidoBotonAtras.play()
          pygame.quit()
          sys.exit()

    pygame.display.update()
main_menu()
import pygame
from pygame.locals import *
from configuracion import *

def letra(size): # carga el tipo de fuente y el tamaño deseado
  return pygame.font.Font("Fuentes/font.ttf", size)

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos): #dibuja la candidata, el tiempo y el puntaje en la pantalla juego

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 380
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_TIEMPO_FINAL), (pos, 100))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS), (pos, 100))
        pos = pos + TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (550, 680))
    screen.blit(ren2, (1160, 10))
    screen.blit(ren3, (10, 10))
    
def dibujarIngresadas(listaIngresadas, screen): #dibuja al costado derecho de la pantalla de juego las palabras ingresadas
    ingresadas_texto = letra(20).render("INGRESADAS", True, "White")
    ingresadas_pos = ingresadas_texto.get_rect(center=(110, 250))
    screen.blit(ingresadas_texto, ingresadas_pos)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    cont = 0
    for i in listaIngresadas:
        cont += 1
        if cont == 1:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 275))
        if cont == 2:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 300))
        if cont == 3:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 325))
        if cont == 4:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 350))
        if cont == 5:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 375))
        if cont == 6:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 400))
        if cont == 7:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 425))
        if cont == 8:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 450))
        if cont == 9:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 475))
        if cont == 10:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 500))
        if cont == 11:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 525))
        if cont == 12:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 550))
        if cont == 13:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 575))
        if cont == 14:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 600))
        if cont == 15:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (10, 625))
        if cont == 16:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 275))
        if cont == 17:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 300))
        if cont == 18:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 325))
        if cont == 19:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 350))
        if cont == 20:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 375))
        if cont == 21:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 400))
        if cont == 22:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 425))
        if cont == 23:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 450))
        if cont == 24:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 475))
        if cont == 25:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 500))
        if cont == 26:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 525))
        if cont == 27:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 550))
        if cont == 28:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 575))
        if cont == 29:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 600))
        if cont == 30:
            ingresadas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(ingresadas, (140, 625))
            

def dibujarCorrectas(listaCorrectas, screen): #dibuja al costado izquierdo de pantalla de juego las palabras correctas ingresadas
    ingresadas_texto = letra(20).render("CORRECTAS", True, "White")
    ingresadas_pos = ingresadas_texto.get_rect(center=(1180, 250))
    screen.blit(ingresadas_texto, ingresadas_pos)
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    cont = 0
    for i in listaCorrectas:
        cont += 1
        if cont == 1:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 275))
        if cont == 2:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 300))
        if cont == 3:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 325))
        if cont == 4:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 350))
        if cont == 5:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 375))
        if cont == 6:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 400))
        if cont == 7:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 425))
        if cont == 8:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 450))
        if cont == 9:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 475))
        if cont == 10:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 500))
        if cont == 11:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 525))
        if cont == 12:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 550))
        if cont == 13:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 575))
        if cont == 14:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 600))
        if cont == 15:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1090, 625))
        if cont == 16:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 275))
        if cont == 17:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 300))
        if cont == 18:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 325))
        if cont == 19:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 350))
        if cont == 20:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 375))
        if cont == 21:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 400))
        if cont == 22:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 425))
        if cont == 23:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 450))
        if cont == 24:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 475))
        if cont == 25:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 500))
        if cont == 26:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 525))
        if cont == 27:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 550))
        if cont == 28:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 575))
        if cont == 29:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 600))
        if cont == 30:
            correctas = defaultFont.render(i, 1, COLOR_TEXTO)
            screen.blit(correctas, (1200, 625))
            
def dibujarNombre(screen, candidata): #dibuja el nombre del usuario que jugó
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 60)
    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    screen.blit(ren1, (500, 320))
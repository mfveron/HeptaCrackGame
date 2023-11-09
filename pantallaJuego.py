import pygame
from configuracion import *
from funcionesRESUELTO import *
from extras import *
from pantallaCorrectas import *

#juego
def jugar(screen, dificultad, tipo, longitud, tiempo): #crea la pantalla del juego en sí, con todos los eventos que se producen en él
    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0
    candidata = ""
    diccionario = []
    palabrasAcertadas = []
    palabrasIngresadas = []

    #lee el diccionario
    lectura(diccionario, tipo)

    #elige las 7 letras al azar y una de ellas como principal
    letrasEnPantalla = dame7Letras()
    letraPrincipal = dameLetra(letrasEnPantalla)

    #se queda con 7 letras que permitan armar muchas palabras, evita que el juego sea aburrido
    while(len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud)) not in dificultad):
        letrasEnPantalla = dame7Letras()
        letraPrincipal = dameLetra(letrasEnPantalla)

    print(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud))
    
    #dibuja la pantalla la primera vez
    dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
    
    #carga el sonido
    sonidoCorrecto = pygame.mixer.Sound("Sonidos/correcto.mp3")
    sonidoIncorrecto = pygame.mixer.Sound("Sonidos/incorrecto.mp3")
    sonidoAmazing = pygame.mixer.Sound("Sonidos/amazing.mp3")
    sonidoIncredible = pygame.mixer.Sound("Sonidos/incredible.mp3")
    sonidoTecla = pygame.mixer.Sound("Sonidos/tecla.mp3")
    
    while segundos > fps/1000:
    # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        #Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            #QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return()

            #Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                sonidoTecla.play()
                letra = dameLetraApretada(e.key)
                candidata += letra   #va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    candidata = candidata[0:len(candidata)-1] #borra la ultima
                if e.key == K_RETURN:  #presionó enter
                    
                    #agrega la candidata a la lista de palabrasIngresadas
                    if candidata not in palabrasIngresadas: 
                        palabrasIngresadas.append(candidata)
                    else:
                        #reproduce el sonido incorrecto
                        sonidoIncorrecto.play()
                        
                    #si es correcta y no esta repetida agrega candidata a la lista de palabrasAcertadas y la procesa, sino resta
                    if candidata in dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud) and candidata not in palabrasAcertadas:
                        palabrasAcertadas.append(candidata)
                        #procesa los puntos
                        puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, longitud)
                        #reproduce el sonido correcto
                        if len(candidata) == 7:
                            sonidoAmazing.play()
                        elif len(candidata) > 7:
                            sonidoIncredible.play()
                        else:
                            sonidoCorrecto.play()
                    elif candidata not in dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud):
                        puntos += procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, longitud)
                        #reproduce el sonido incorrecto
                        sonidoIncorrecto.play()
                    
                    #resetea candidata
                    candidata = ""
        #A TIEMPO_MAX le sumamos el tiempo que el usuario estuvo navegando en el menu
        segundos = (TIEMPO_MAX + tiempo/1000) - pygame.time.get_ticks()/1000  #tiempo en segundos
        
        
        #cargar la imagen de fondo
        imagenMenu = pygame.image.load("Imagenes/D0.png")
    
        screen.blit(imagenMenu, (0, 0))

        #Dibujar de nuevo todo
        dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos)
        
        #dibuja la candidata a la izquierda de la pantalla
        dibujarIngresadas(palabrasIngresadas, screen)
        
        #dibuja la candidata correcta a la derecha de la pantalla
        dibujarCorrectas(palabrasAcertadas, screen)
        
        if len(dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud)) == len(palabrasAcertadas):
            crearHistorialPuntaje(puntos)
            from pantallaGanador import win
            win(screen)
    
        pygame.display.flip()
        
    #si se acaba el tiempo se ejecuta la pantalla de game over    
    if segundos < fps/1000:
        crearHistorialPuntaje(puntos)
        gameOver(screen, palabrasAcertadas)
        
    while 1:
        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return


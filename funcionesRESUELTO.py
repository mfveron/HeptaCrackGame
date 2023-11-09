from pantallaJuego import *
from configuracion import *
import random

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario, tipo):
  if tipo == "normal":
    lemario = open("lemario.txt", "r")
    for palabras in lemario:
      palabras = palabras[0:-1]
      diccionario.append(palabras)
    lemario.close()
  elif tipo == "nombres":
    nombres = open("nombresApellidos.txt", "r", encoding="utf-8")
    for palabras in nombres:
      palabras = palabras[0:-1]
      diccionario.append(palabras)
    nombres.close()
  elif tipo == "paises":
    paises = open("paisesCiudades.txt", "r", encoding="utf-8")
    for palabras in paises:
      palabras = palabras[0:-1]
      diccionario.append(palabras)
    paises.close()

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
  cant_vocales = random.randint(2,3)
  if cant_vocales == 2:
      cadena=asignarLetras(cant_vocales)
  elif cant_vocales == 3:
      cadena=asignarLetras(cant_vocales)
  return cadena

#genera las letras de la cadena que cumplen las condiciones, segun una cantidad de vocales elegida al azar entre 2 y 3
def asignarLetras(cant_vocales):
    consonantes = "qwrtpsdfghjlcvbnmkxyz"
    vocales = "aeiou"
    dificiles = "kxyz"
    cont_dificiles = 0
    cadena = ""
    while len(cadena) < cant_vocales: #primero me aseguro de que la cadena tenga las vocales necesarias
        vocal = random.choice(vocales)
        if vocal not in cadena:
            cadena += vocal
    while len(cadena) >= cant_vocales and len(cadena) <7: #la completo con consonantes, cuidando que no haya mas de una dificil
        consonante = random.choice(consonantes)
        if consonante in dificiles:
            cont_dificiles += 1
            if consonante not in cadena and cont_dificiles <= 1:
                cadena += consonante
        elif consonante not in dificiles and consonante not in cadena:
            cadena += consonante
    return cadena

def dameLetra(letrasEnPantalla): #elige una letra de las letras en pantalla
  azar = random.choice(letrasEnPantalla)
  return azar
  
#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario, longitud):
  if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, longitud):
    return Puntos(candidata)
  else:
    return -1
  
#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario, longitud):
  if candidata in dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud):
    return True
  else:
    return False

#devuelve los puntos
def Puntos(candidata):
    if len(candidata) == 3:
        return 1
    if len(candidata) == 4:
        return 2
    if len(candidata) >= 5 and len(candidata) != 7:
        return len(candidata)
    if len(candidata) == 7 :
        return 10

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario, longitud):
    correctas = []
    for elemento in diccionario:
      cumple = cumpleRequisitos(letraPrincipal, letrasEnPantalla, elemento, longitud)
      if cumple == True:
        correctas.append(elemento)
    return correctas

#verifica que una palabra contenga la letra principal y este compuesta solo de las letras en pantalla
def cumpleRequisitos(letraPrincipal, letrasEnPantalla, palabra, longitud):
  tieneLetraEnPantalla = 0
  tienePrincipal = 0
  for letra in palabra:
    if letra in letrasEnPantalla:
      tieneLetraEnPantalla += 1
    if letra == letraPrincipal:
      tienePrincipal += 1
  if len(palabra) == tieneLetraEnPantalla and tienePrincipal > 0 and len(palabra) >= longitud:
    return True

#crea un archivo txt para ir guardando los puntajes
def crearHistorialPuntaje(puntaje):
    historial = open("historialPuntajes.txt", "a")
    historial.write(str(puntaje)+"\n")
    historial.close()

#accede al archivo anteriormente creado para leerlo y cargarlo
def lecHistorialPuntaje(ranking):
    historial = open("historialPuntajes.txt", "r")
    for puntajes in historial:
      puntajes = puntajes[0:-1]
      ranking.append(puntajes)
    historial.close()

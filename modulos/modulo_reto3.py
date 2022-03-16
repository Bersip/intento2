import random
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


palabras = 'color mar charca cenote profundidad sagrado ritual blue maya cielo'.split()


##############################
##Esta funcion retorna una palabra aleatoria.
##############################
def buscarPalabraAleat(listaPalabras):
    # Esta funcion retorna una palabra aleatoria.
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]


##############################
##Esta funcion
##############################
def displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta):
    print(AHORCADO[len(letraIncorrecta)])
    print ("")
    fin = " "
    print ('Letras incorrectas:', fin)
    for letra in letraIncorrecta:
        print (letra, fin)
    print ("")
    espacio = '_' * len(palabraSecreta)
    for i in range(len(palabraSecreta)): # Remplaza los espacios en blanco por la letra bien escrita
        if palabraSecreta[i] in letraCorrecta:
            espacio = espacio[:i] + palabraSecreta[i] + espacio[i+1:]
    for letra in espacio: # Mostrará la palabra secreta con espacios entre letras
        print (letra, fin)
    print ("")
 
def elijeLetra(algunaLetra):
    # Devuelve la letra que el jugador ingreso. Esta función hace que el jugador ingrese una letra y no cualquier otra cosa
    while True:
        print ('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduce una sola letra.') 
        elif letra in algunaLetra:
            print ('Ya has elegido esa letra ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Elije una letra.')
        else:
            return letra
 
def empezar():
    # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
    print ('¿Quieres más pistas? (Si o No)')
    return input().lower().startswith('s')


def puerta3():
    print("")
    print("")
    print("")
    print ("¡Excelente aventurero! Ya estás muy cerca de saber ¿en dónde estás?.")
    print("                  3er reto: el ahorcado                    ")
    print("")
    
    print("")
    print("")
    print("Había una vez en la cercanías del lago _________(reto 2 pista 3).")
    print("Un antiguo sitio que se utilizaba como centro ceremonial Maya. Son")
    print("unas aguas cristalinas que tienen alrededor de 3000 años.")
    print("")
    print("En una mañana un aventurero llegó a ese místico lugar. Quedó anodadado")
    print("de la espléndida belleza natural en la que se encontraba y se preguntaba")
    print("como se llama. Entonces al alzar la vista observó a un peculiar hombre")
    print("con plumas y de piel canela, quién le dijo: ¡Juguemos! y te daré algunas.")
    print("pistas.")
    
    while (True): 
        jugar = input ("¿Aceptas el reto? Sino, tipea salir: ")
        
        if(jugar =="salir"):
            pasalir=True
            return pasalir
     
        if(jugar =="si"):      
            print("")
            print("E L  A H O R C A D O")
            break
        else:
            print("")
            print("Debes escribir si o salir.")

    letraIncorrecta = ""
    letraCorrecta = ""
    palabraSecreta = buscarPalabraAleat(palabras)
    finJuego = False
    
    while True:
        displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
        # El usuairo elije una letra.
        letra = elijeLetra(letraIncorrecta + letraCorrecta)
        if letra in palabraSecreta:
            letraCorrecta = letraCorrecta + letra
            # Se fija si el jugador ganó
            letrasEncontradas = True
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i] not in letraCorrecta:
                    letrasEncontradas = False
                    break
            if letrasEncontradas:
                print ('¡Muy bien! La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
                finJuego = True
        else:
            letraIncorrecta = letraIncorrecta + letra
            # Comprueba la cantidad de letras que ha ingresado el jugador y si perdió
            if len(letraIncorrecta) == len(AHORCADO) - 1:
                displayBoard(AHORCADO, letraIncorrecta, letraCorrecta, palabraSecreta)
                print ('¡Se ha quedado sin letras!\nDespues de ' + str(len(letraIncorrecta)) + ' letras erróneas y ' + str(len(letraCorrecta)) + ' letras correctas, la palabra era "' + palabraSecreta + '"')
                finJuego = True
        
        # Pregunta al jugador si quiere jugar de nuevo
        if finJuego:
            if empezar():
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
                palabraSecreta = buscarPalabraAleat(palabras)
            else:
                break
    
    print("")
    print("Acaso ¿ya sabes la respuesta?")
    while (True): 
       yasabe = input ("")
       
       if(yasabe =="no"):
           yasabe=True
           return puerta3()
    
       if(yasabe =="si"):      
           print("")
           print("¡Enhorabuena!")
           print("")
           break
       else:
           print("")
           print("Debes escribir si o no.")

      
    pasalir=False
    return pasalir
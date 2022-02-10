import random
import string #Contiene todas las letras mayusculas y minusculas

nivel ={ #diccionario de niveles, especifica los limites maximos del numero random
    "1" : 10,
    "2" : 50,
    "3" : 100,
    "4" : 1000
}

vidas ={ #diccionario de numero de oportunidades (vidas), según el nivel
    "1":4,
    "2":6,
    "3":8,
    "4":10
}

lista_magica =[] #lista para guardar la palabra magica
    
def juego(lim_max,option,nvida,acumulado):
    numero_random = random.randint (1,lim_max)
    lives = nvida+acumulado
    numero = int (input("Estas en el nivel " + str(option) + ", juegas en un rango entre 1 y " + str(lim_max) + ". Te quedan " + str(lives) +" oportunidades. Elige un número: "))  
    while numero != numero_random:
        lives-=1
        if lives == 0:
            numero = (input("Perdiooo. El número correcto es " + str(numero_random))) #si pierde el juego, ofrece diferentes opciones
            revancha=int(input("""¿Desea juegar otra vez?
            1- El mismo nivel.
            2- Desde el principio (nivel 1).
            3- Seleccionar el nivel.
            4- No quiero jugar mas.
            """))
            if revancha == 1:
                opciones(option) #opcion sigue teniendo el mismo valor anterior
            elif revancha ==2:
                option = 1 #reinicia los niveles
                opciones(option)
            elif revancha == 3:
                option = int(input("Elige un nivel: ")) #Elige el nivel
                opciones(option)
            elif revancha == 4:
                print("Gracias por jugar, perdedor de mierda")
            else:
                print("Opcion incorrecta")
            break
        elif numero < numero_random:
            numero = int (input("Te quedan " + str(lives) + " vidas. Elige un numero mayor. "))
        elif numero > numero_random:
            numero = int (input("Te quedan " + str(lives) + " vidas. Elige un numero menor. "))
    else:
        option=option+1 #Define si terminó los niveles del juego
        if option <= 4:
            print ("Ganaste! El número " + str(numero) + " es correcto. Avanzaste al nivel " + str(option) + ". Acumulas " + str(lives) + " vidas, para la siguiente ronda")
            acumulado = lives #sirve para guardar las vidas que no se utilizaron y sumarlas para el siguiente nivel
            opciones(option,acumulado)
        else:
            print("¡Ganaste! El número " + str(numero) +" es correcto. Felicitaciones, terminaste el juego.")      

def opciones(option, acumulado): #la tercera funcion. llama de los diccionarios el número de vidas, dificultad y envia a la funcion juego
    if option == 1:
        juego(nivel["1"], option, vidas["1"], acumulado) #nivel para seleccionar los limites maximos, opción es decir el nivel, numero de oportunidades
    elif option ==2:
        juego(nivel["2"], option, vidas["2"], acumulado)
    elif option ==3:
        juego(nivel["3"], option, vidas["3"], acumulado)
    elif option ==4:
        juego(nivel["4"], option, vidas["4"], acumulado)
    else:
        numero=input("Opción incorrecta.")

def magia (palabra_magica, option):
    palabra_magica = palabra_magica[0:9] #slice
    palabra_random = ''.join(random.sample(string.ascii_lowercase,10))
    contador= 0
    for x in range (0,9): 
        lista_magica.append(palabra_magica[x]) #agrega cada caracter a la lista magica
   
    for i in range (0,9):
        if (palabra_random[i]) in lista_magica: #comprueba si el caracter de la palabra random está en la lista magica
            contador = contador + 1
        else:
            continue
    print("Obtuvo un bono de " + str(contador) + " (vidas) para esta partida" )
    
    opciones(option, contador)

def run():
    
    menu = """ 
    Bienvenido a __ADIVINA EL NUMERO__

    Elige el nivel de dificultad, por favor:

    1 - Fácil.       [Rango 1 - 10]
    2 - Medio.       [Rango 1 - 50]
    3 - Dificil.     [Rango 1 - 100]
    4 - Muy dificil  [Rango 1 - 1000]

        **** _ 
    """
    #define la primera funcion, el nivel de dificultad. Envia hacia la función opciones
    option = int(input(menu))
    palabra_magica = str(input("Ahora, escribe una palabra magica de 10 letras: ")).strip().lower() #palabra+correctores de texto
    
    magia(str(palabra_magica), option)
        
    #opciones(option,acumulado)     

if __name__ == "__main__":
    run()
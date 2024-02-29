#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?
import random
acierto=0
lista2=[]
fin=0
veces=8
partidas=0
punt=0
puntuacion=0
lista1=["casa,barco,gato,perro,madera,agua,puente,pantalón"]
x=lista1[0]
esplit=x.split(",")
while fin==0:
    palabra=(esplit[random.randint(0,7)])
    while acierto==0:
        adivinar=input("Introduce la palabra que crees que puede ser:")
        if adivinar==palabra:
            acierto=+1
            print("Has acertado la palabra")
            puntuacion=puntuacion+veces
            punt=punt+veces
            lista2.append(puntuacion)
            veces=8
            partidas=partidas+1
            fin=int(input("¿Quieres acabar la partida? 0 para no, 1 para si:"))
            if fin==0:
                acierto=0
                palabra=(esplit[random.randint(0,7)])
                puntuacion=0
        else:
            print("No has adivinado la palabra, sigue probando")
            veces=veces-1
if fin==1:
    print("Puntuación:",lista2)
    print("Tu puntuación ha sido de",punt)
    print("La media total de las partidas realizadas es de",partidas*4)
    if punt>(partidas*4):
        print("Tienes buena suerte")
    else:
        print("Dedícate al parchís")
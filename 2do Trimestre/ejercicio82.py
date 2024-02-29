#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
import random
acierto=0
lista1=["casa,barco,gato,perro,madera,agua,puente,pantalón"]
x=lista1[0]
esplit=x.split(",")
palabra=(esplit[random.randint(0,7)])
while acierto==0:
    adivinar=input("Introduce la palabra que crees que puede ser:")
    if adivinar==palabra:
        acierto=+1
        print("Has acertado la palabra")
    else:
        print("No has adivinado la palabra, sigue probando")
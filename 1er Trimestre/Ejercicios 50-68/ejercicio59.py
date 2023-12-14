#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
var1=random.randint(1,1000)
acierto=0
intentos=0
while acierto!=1:
    intentos=intentos+1
    var2=int(input("Introduce el número que piensas que es el correcto:"))
    if var2==var1:
        print("Has acertado el número")
        acierto=acierto+1
    if var2>var1:
        print("El número seleccionado es incorrecto, y el número es mayor que el número oculto")
    else:
        print("El número seleccionado es incorrecto, el número seleccionado es menor que el número oculto")
print("El número de intentos ha sido de",intentos,"intentos")
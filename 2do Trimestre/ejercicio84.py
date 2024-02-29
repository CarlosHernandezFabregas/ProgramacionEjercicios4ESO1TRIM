#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.

import random
lista1=["casa,barco,gato,perro,madera,agua,puente,pantalón"]
x=lista1[0]
lista2=[]
pos=0
esplit=x.split(",")
var=0
veces=0
intentos=3
var=esplit[random.randint(0,7)]
lista2.append(var)
y=lista2.index(var)
listamin=[]
for cont in var:
    listamin.append(cont)
listamin.sort(reverse=True)
print(listamin)
acierto=0
while acierto!=var and veces<3:
    acierto=input("Introduce una palabra correcta:")
    if acierto!=var:
        intentos=intentos-1
        print("No has acertado la palabra. Te quedan",intentos,"intentos")
        veces=veces+1
    else:print("Has acertado la palabra al intento número",veces+1)
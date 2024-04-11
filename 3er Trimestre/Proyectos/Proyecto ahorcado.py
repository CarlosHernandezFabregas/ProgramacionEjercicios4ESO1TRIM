#AHORCADO Diseña un programa que simule el juego del Ahorcado teniendo en cuenta las indicaciones descritas en
#los siguientes bloques.
import random
import time
start=time.perf_counter()
lista_palabrasecreta=["casa","coche","lavadora","titanic","supermercado","episodio","telenovela","jardinero","amapola","guarderia"]
lista_partida=[]
lista_ahorcado=[]
palabracorrecta=[]
lista_fin=["A","H","O","R","C","A","D","O"]
lista_aciertos=[]
lista_errores=[]
fin=0
x=0
pos=0
fallo=0
veces=0
acierto=0
num=random.randint(0,9)
palabra=lista_palabrasecreta[num]
for cont in palabra:
    palabracorrecta.append(cont)
for cont in range(len(palabra)):
    lista_partida.append("_")
print(lista_partida)
while lista_ahorcado!=lista_fin and lista_partida!=palabracorrecta: #Primer bucle para establecer que no se ha acabado
    letras=input("Introduce una letra que se introduzca en la palabra:")
    letras=letras.lower()
    x=1
    fallo=0
    acierto=0
    for cont in range(len(palabra)): #Para recorrer el string
        if letras==palabra[cont]:
            x=palabra.count(letras)
            lista_partida.pop(cont)
            lista_partida.insert(cont,letras)
            acierto=acierto+1
            veces=veces+1
            fallo=0
            lista_aciertos.append(letras)
        if palabra.count(letras)<1: #Si la letra no está en la palabra, que solo haya 1 error
            fallo=fallo+1
        if x!=acierto and fallo==1:
                fallo=fallo+1
                if veces!=len(palabra):
                    lista_ahorcado.append(lista_fin[pos])
                    pos=pos+1
                    lista_errores.append(letras)
                    print(lista_ahorcado)
                    if len(lista_ahorcado)==8:
                         fin=1
    if lista_ahorcado==lista_fin or lista_partida==palabracorrecta: #Si cualquiera de las 2 listas está completa, que se acabe la partida
        fin=1
    print(lista_partida)
    if fin==1:
        final=time.perf_counter()-start
        print("El número de aciertos ha sido de",len(lista_aciertos))
        print("El número de errores ha sido de",len(lista_errores))
        print("El tiempo que se ha tardado ha sido de",final)
        repe=input("¿Quieres hacer una nueva partida? si para si, no para no:") #Para hacer una nueva partida
        if repe=="si": #Se reinician todas las variables
            fin=0
            veces=0
            acierto=0
            fallo=0
            pos=0
            lista_palabrasecreta.pop(num)
            preg=input("¿Deseas introducir una nueva palabra? si para si, no para no") #Para introducir una nueva palabra
            if preg=="si":
                lista_palabrasecreta.insert(num,input("Introduce la nueva palabra que quieres que se añada a la lista:"))
            num=random.randint(0,9)
            palabra=lista_palabrasecreta[num]
            cont=0
            x=0
            lista_ahorcado=[]
            lista_partida=[]
            palabracorrecta=[]
            lista_aciertos=[]
            lista_errores=[]
            for cont in palabra:
                palabracorrecta.append(cont)
            for cont in range(len(palabra)):
                lista_partida.append("_")
            print(lista_partida)
            start=time.perf_counter()
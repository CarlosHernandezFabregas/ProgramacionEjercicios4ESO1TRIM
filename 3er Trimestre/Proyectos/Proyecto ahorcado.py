#AHORCADO Diseña un programa que simule el juego del Ahorcado teniendo en cuenta las indicaciones descritas en
#los siguientes bloques.
import random
lista_palabrasecreta=["casa","coche","lavadora","titanic","supermercado","episodio","telenovela","jardinero","amapola","guarderia"]
lista_partida=[]
lista_ahorcado=[]
palabracorrecta=[]
lista_fin=["A","H","O","R","C","A","D","O"]
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
while lista_ahorcado!=lista_fin and lista_partida!=palabracorrecta:
    letras=input("Introduce una letra que se introduzca en la palabra:")
    acierto=0
    for cont in range(len(palabra)):
        if letras==palabra[cont]:
            x=palabra.count(letras)
            lista_partida.pop(cont)
            lista_partida.insert(cont,letras)
            acierto=acierto+1
            veces=veces+1
    if x!=acierto:
                fallo=fallo+1
                if veces!=7:
                    lista_ahorcado.append(lista_fin[pos])
                    pos=pos+1
                    print(lista_ahorcado)
                    if len(lista_ahorcado)==8:
                         fin=1
    if lista_ahorcado==lista_fin or lista_partida==palabracorrecta:
        fin=1
    print(lista_partida)
    if fin==1:
        repe=input("¿Quieres hacer una nueva partida? si para si, no para no:")
        if repe=="si":
            fin=0
            veces=0
            acierto=0
            fallo=0
            pos=0
            lista_palabrasecreta.pop(num)
            lista_palabrasecreta.insert(num,input("Introduce la nueva palabra que quieres que se añada a la lista:"))
            num=random.randint(0,9)
            palabra=lista_palabrasecreta[num]
            cont=0
            x=0
            lista_ahorcado=[]
            lista_partida=[]
            palabracorrecta=[]
            for cont in palabra:
                palabracorrecta.append(cont)
            for cont in range(len(palabra)):
                lista_partida.append("_")
            print(lista_partida)
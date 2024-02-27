#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo.

lista1=[]
lista2=[]
pal=int(input("introduce el numero de palabras:"))
reps=0
while reps<pal:
    tot=input("introduce una palabra:")
    lista1.append(tot)
    lista2.append(tot)
    reps=reps+1
lista1.sort()
lista2.sort(reverse= True)
print(lista1)
print(lista2)
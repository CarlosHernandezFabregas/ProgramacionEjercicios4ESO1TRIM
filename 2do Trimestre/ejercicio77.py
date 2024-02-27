#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
sum=len(lista1)
lista2=[]
cont=0
min=[]
may=[]
lista3=[]
listamay=[]
alfavar=""
betavar=""
num=0
orden=0

for cont in range(sum):
    if lista1[cont].isupper():
        betavar=lista1[cont].lower()
        listamay.append(lista1[cont])
        may.append(lista1[cont])
        may.remove(may[num])
        may.append(betavar)
        num=+1
    if lista1[cont].isalpha() and lista1[cont].islower():
        min.append(lista1[cont])
    if lista1[cont].isnumeric():
        lista3.append(lista1[cont])
longm=len(may)
lista2.extend(min)
lista2.extend(may)
lista2.sort()
for cont in range(longm):
    x=lista2.index(may[cont])
    lista2.insert(x,listamay[cont]) # ******* REPASAR: INDEX TE SIRVE PARA SABER LA POSICION, POR LO TANTO, PUEDES AÑADIR VARIABLES EN LA LISTA EN ESA POSICION
    lista2.remove(may[cont])
orden=int(input("¿Quieres ver la lista ordenada o al revés? 1 si la quieres ordenada, 2 si la quieres al revés:"))
if orden==1:
    lista3.sort()
    print(lista3)
    print(lista2)
if orden==2:
    lista3.sort(reverse=True)
    print(lista3)
    lista2.reverse()
    print(lista2)
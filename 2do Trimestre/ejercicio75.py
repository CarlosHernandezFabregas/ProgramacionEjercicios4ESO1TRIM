#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numéricos
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
sum=len(lista1)
cont=0
numeros=0
letras=0
mayusc=0
sumatot=0
numerost=0
for cont in range(sum):
    if lista1[cont].isalpha():
        letras=letras+1
    if lista1[cont].isnumeric():
        numeros=numeros+1
    if lista1[cont].isupper():
        mayusc=mayusc+1
    if lista1[cont].isnumeric():
        numerost=numerost+int(lista1[cont])

print("La cantidad total de valores de la lista es",sum)
print("la cantidad total de números es de",numeros)
print("La cantidad de letras total es de",letras)
print("La cantidad total de mayúsculas es de",mayusc)
print("La suma total de los números es de",numerost)
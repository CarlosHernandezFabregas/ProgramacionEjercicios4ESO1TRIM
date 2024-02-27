#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
rep="si"
lista=[]
x=0
while rep!="no":
    letra=input("Introduce una letra:")
    x=lista.count(letra)
    
    if letra.isnumeric()!=True and x<=0:
        lista.append(letra)
    
    rep=input("Quieres repetir? si/no:")
print(lista)
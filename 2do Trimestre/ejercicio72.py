#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
rep="si"
lista=[]
x=0
while rep!="no":
    letra=input("Introduce una letra:")
    
    if letra=="á" or letra=="à":
        letra="a"
    if letra=="é" or letra=="è":
        letra="e"
    if letra=="í" or letra=="ì":
        letra="i"
    if letra=="ó" or letra=="ò":
        letra="o"
    if letra=="ú" or letra=="ù":
        letra="u"
        
    x=lista.count(letra)
    if letra.isnumeric()!=True and x<=0:
        lista.append(letra)
    
    rep=input("Quieres repetir? si/no:")
print(lista)
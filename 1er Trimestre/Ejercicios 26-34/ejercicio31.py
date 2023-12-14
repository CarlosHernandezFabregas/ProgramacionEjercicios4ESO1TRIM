#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
var1=str(input("Introduce la frase:A quién madruga Dios ayuda"))
a=var1.find("A")
quién=var1.find("quién")
madruga=var1.find("madruga")
Dios=var1.find("Dios")
ayuda=var1.find("ayuda")
if a>=0 and quién>=0 and madruga>=0 and Dios>=0 and ayuda>=0:
    print("Están todas las palabras")
else:
    print("Algo falta en la frase")
#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
var=str(input("Introduce la frase:(A quién madruga Dios ayuda) ,"))
var1=var.lower()
a=var1.find("a")
quién=var1.find("quién")
madruga=var1.find("madruga")
Dios=var1.find("dios")
ayuda=var1.find("ayuda")
if a>=0 and quién>=0 and madruga>=0 and Dios>=0 and ayuda>=0:
    print("Están todas las palabras")
else:
    print("Algo falta en la frase")
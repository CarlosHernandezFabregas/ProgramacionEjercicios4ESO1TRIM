#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
var1=float(input("Introduce tu altura en metros"))
var2=var1**2
var3=float(input("introduce tu peso en kg"))
if(var3/var2)>25:print("Tienes sobrepeso, haz dieta")
else:print("Enhorabuena, no tienes sobrepeso")

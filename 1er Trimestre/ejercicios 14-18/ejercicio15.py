#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
var1=int(input("introduce el radio del cilindro"))
var2=int(input("Introduce la altura del cilindro"))
var3=math.pi
var4=(var3*var2)*2
var5=(round(2*((var3*(var1**2))+(var4)),2))
print("El área del círculo es",var5)
var6=round(var3*(var1**2)*var2,(2))
print(var6)




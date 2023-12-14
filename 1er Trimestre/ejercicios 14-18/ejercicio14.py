#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo.
#Redondea el resultado a un decimal.
import math
var1=int(input("Introduce el diámetro del círculo"))
var3=math.pi
var5=var1/2
var2=round((var5**2)*var3,1)
print("El área del círculo es",var2)
var4=round(2*var3*var1/2,1)
print("El perímetro del círculo es",var4)



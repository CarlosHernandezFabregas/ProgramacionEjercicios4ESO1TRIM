#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
print("El cociente de los dos números es",var1/var2,".El resto de los dos números es",var1%var2)
if(var1%2==0):print("El dividendo es par")
else:print("El dividendo es impar")

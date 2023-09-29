#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=int(input("Introduce el valor de la primera variable"))
b=int(input("Introduce el valor de la segunda variable"))
c=int(input("introduce el valor del término independiente"))
xx1=math.sqrt (b**2)-(4*a*c)
xy1=2*a
x1=-b+xx1/xy1
print(("El primer valor de x es"):x1)
xx2=math.sqrt (b**2)-(4*a*c)
x2=b-xx2/xy1
print(("El segundo valor de x es"), x2)
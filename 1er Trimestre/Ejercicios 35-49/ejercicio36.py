#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario
var_n=int(input("Introduce el numero de numeros naturales que quieres sumar"))
num=0
contador=0
for cont in range(var_n):
    num=num+1+contador
    contador=contador+1
print(num)
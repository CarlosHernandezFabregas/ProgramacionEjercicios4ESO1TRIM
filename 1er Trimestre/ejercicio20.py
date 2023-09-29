#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
num1=int(input("Introduce un número"))
num2=int(input("Introduce otro número"))
if (num1 or num2)<0 and (num1 or num2)>10:
    print("No se puede ejecutar el programa")
elif num1<num2:
    print("El primer número es menor que el segundo")
elif num1>num2:
    print("El primer número es mayor que el segundo")
else:
    print("El primer número es igual que el segundo")
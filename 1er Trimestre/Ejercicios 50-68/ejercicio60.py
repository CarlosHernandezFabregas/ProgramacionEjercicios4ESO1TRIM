#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
var1=int(input("Introduce un número"))
mult=0
var2=0
while mult<=10:
    var2=var1*mult
    mult=mult+1
    print(var2)
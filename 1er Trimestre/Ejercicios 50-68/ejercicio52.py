#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
var3="s"
var3=var3.lower()
var4=0
while var3=="s":
    var4=var1+var2
    print("El resultado es:",var4)
    var3=str(input("Quieres seguir con el programa? s/n"))
    if var3!="s":print("Programa finalizado")
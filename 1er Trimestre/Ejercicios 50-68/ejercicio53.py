#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
var3="s"
var3=var3.lower()
var4=0
nsumas=0
nreps=0
while var3=="s":
    var4=var1+var2
    print("El resultado es:",var4)
    nsumas=nsumas+var4
    nreps=nreps+1
    var3=str(input("Quieres seguir con el programa? s/n"))
    if var3!="s":print("Programa finalizado")
print("La suma de todos los numeros que has sumado son:",nsumas)
print("El número de repeticiones del programa son:",nreps)
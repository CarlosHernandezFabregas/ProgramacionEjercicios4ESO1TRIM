#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
var3="s"
var3=var3.lower()
var4=0
nsumas=0
nreps=0
while nsumas>50 or nsumas%2==0:
    var4=var1+var2
    print("El resultado es:",var4)
    nsumas=nsumas+var4
    print(nsumas)
    nreps=nreps+1
    if nsumas>50 or nsumas%2==0:
        var1=int(input("Introduce el primer número"))
        var2=int(input("Introduce el segundo número"))
    else:break
print("La suma de todos los numeros que has sumado son:",nsumas)
print("El número de repeticiones del programa son:",nreps)
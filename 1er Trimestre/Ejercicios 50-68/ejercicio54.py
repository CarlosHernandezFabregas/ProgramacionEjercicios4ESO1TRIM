#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
var3="s"
var3=var3.lower()
var4=0
nsumas=0
nreps=0
while nsumas<=50:
    var4=var1+var2
    print("El resultado es:",var4)
    nsumas=nsumas+var4
    print(nsumas)
    nreps=nreps+1
    if nsumas<50:
        var1=int(input("Introduce el primer número"))
        var2=int(input("Introduce el segundo número"))
    else:break
print("La suma de todos los numeros que has sumado son:",nsumas)
print("El número de repeticiones del programa son:",nreps)
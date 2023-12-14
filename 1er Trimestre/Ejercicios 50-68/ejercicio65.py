#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayor y cuál el menor.
var1=int(input("Introduce un valor"))
par=0
impar=0
negativos=0
positivos=0
cero=0
total=0
pik=0
mayor=-9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
menor=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while var1!=-99:
    if var1>mayor:mayor=var1
    if var1<menor:menor=var1
    pik=pik+var1
    if var1%2==0:par=par+1
    if var1%2!=0:impar=impar+1
    if var1<0:negativos=negativos+1
    if var1>0:positivos=positivos+1
    if var1==0:cero=cero+1
    var1=int(input("Introduce un valor"))
print("El total es",pik)
print("El total de impares es de",impar)
print("El total de pares es de",par)
print("El total de negativos es de",negativos)
print("El total de postivos es de",positivos)
print("El total de ceros es de",cero)
print("El número mayor es",mayor)
print("El número menor es",menor)
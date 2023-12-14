#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo valor"))
par=""
impar=""
vez=1
if var2>var1:
    var2=var2+1
    for cont in range(var2-var1):
        var3=var2-vez
        if var3%2==0:
           par=par+str(var3)
        else:
            impar=impar+str(var3)
        vez=vez+1
if var1>var2:
    var1=var1+1
    for cont in range(var1-var2):
        var3=var1-vez
        if var3%2==0:
            par=par+str(var3)
        else:
            impar=impar+str(var3)
        vez=vez+1
print("Los pares son",par)
print("los impares son",impar)
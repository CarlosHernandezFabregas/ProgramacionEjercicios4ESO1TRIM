#40. Crea un programa que cuente todos los números pares hasta el número 50
impar=0
par=0
for cont in range(0,50):
    var1=cont%2
    if var1==0:
        par=par+1
    else:impar=impar+1
print("El número de pares es",par)
print("El número de impares es",impar)
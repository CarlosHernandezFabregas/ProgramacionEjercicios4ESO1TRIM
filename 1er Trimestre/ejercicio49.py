#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
var1=str(input("Introduce una palabra 'secreta':"))
x=0
pos=0
for cont in var1:
    var2=str(input("Introduce una letra"))
    x=var1.find(var2)
    if x>=0:
        print("Has acertado la/s letra/s de la palabra en la posición",x,)
    else:
        print("Has fallado la letra, x intentos restantes")
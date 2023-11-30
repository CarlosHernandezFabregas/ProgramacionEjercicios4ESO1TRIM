#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra.
var1=str(input("Introduce una palabra 'secreta':"))
x=0
for cont in var1:
    var2=str(input("Introduce una letra"))
    x=var1.find(var2)
    if x>=0:
        print("Has acertado la/s letra/s de la palabra")
    else:
        print("Has fallado la letra, x intentos restantes")
#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
var_n=int(input("Introduce el número de notas"))
for cont in range(var_n):
    var_not=float(input("Introduce la nota"))
    if var_not<0 and var_not>10:print("No te pases de listo, calcula con notas reales, del 0 al 10")
    if var_not>=0 and var_not<=10:
        if var_not<=4.9:print("Nota suspendida")
        else:print("Nota aprobada")
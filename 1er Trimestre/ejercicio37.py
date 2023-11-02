#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
var_n=int(input("Introduce el número de notas"))
for cont in range(var_n):
    var_not=float(input("Introduce la nota"))
    if var_not<=4.5:print("Nota suspendida")
    else:print("Nota aprobada")
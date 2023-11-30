#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
var_n=int(input("Introduce un número de números que quieras introducir"))
positivo=0
negativo=0
cero=0
for cont in range(var_n):
    var_tot=float(input("Introduce un número"))
    if var_tot>0:
        positivo=positivo+1
    if var_tot<0:
        negativo=negativo+1
    if var_tot==0:
        cero=cero+1
print("hay",negativo,"números menores que 0") 
print("hay",cero,"números iguales que 0")
print("hay",positivo,"números mayores que 0")

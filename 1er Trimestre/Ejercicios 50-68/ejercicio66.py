#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
veces=0
start=time.perf_counter()
fin=0
while fin<3:
    var1=random.randint(1,6)
    if var1==1:uno=uno+1
    if var1==2:dos=dos+1
    if var1==3:tres=tres+1
    if var1==4:cuatro=cuatro+1
    if var1==5:cinco=cinco+1
    if var1==6:seis=seis+1
    fin=time.perf_counter()-start
print("Uno:",uno)
print("Dos:",dos)
print("Tres:",tres)
print("Cuatro:",cuatro)
print("Cinco:",cinco)
print("Seis:",seis)
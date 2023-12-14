#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
veces=0
while veces<100:
    var1=random.randint(1,6)
    if var1==1:uno=uno+1
    if var1==2:dos=dos+1
    if var1==3:tres=tres+1
    if var1==4:cuatro=cuatro+1
    if var1==5:cinco=cinco+1
    if var1==6:seis=seis+1
    veces=veces+1
print("Uno:",uno)
print("Dos:",dos)
print("Tres:",tres)
print("Cuatro:",cuatro)
print("Cinco:",cinco)
print("Seis:",seis)
#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.
var1=str(input("introduce una palabra,:"))
Pi=""
low=""
for cont in var1:
    if cont.lower()=="a" or cont.lower()=="e" or cont.lower()=="i" or cont.lower()=="o" or cont.lower()=="u":
        Pi=Pi+cont
    else:low=low+cont
print("Las vocales son:",Pi)
print("Las consonantes son:",low)
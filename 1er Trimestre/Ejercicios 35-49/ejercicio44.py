#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,
var1=""
var2=0
for cont in range(0,100,3):
    if cont==99:
        var1=var1+str(cont)
    else:
        var1=var1+str(cont)+","
print(var1)
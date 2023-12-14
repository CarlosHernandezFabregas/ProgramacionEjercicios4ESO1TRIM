#41. Imprime el siguiente patrón utilizando for:
var1=54321
mult=10000
pos=0
num=5
for cont in range(5):
    print(var1)
    var1=var1-(num*mult)
    mult=mult/10
    num=num-1
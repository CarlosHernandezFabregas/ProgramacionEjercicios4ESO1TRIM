#42. Imprima el siguiente patrón con el ciclo for. 
var1="*"
pos=0
num=1
sum="*"
for cont in range(9):
    pos=pos+1
    if pos==1:var1="*"
    if pos==2:var1="**"
    if pos==3:var1="***"
    if pos==4:
        var1="****"
    if pos==5:
        var1="*****"
    if pos==6:
        var1="****"
    if pos==7:
        var1="***"
    if pos==8:
        var1="**"
    if pos==9:
        var1="*"
    print(var1)
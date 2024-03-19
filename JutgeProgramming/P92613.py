x=input()
lista=x.split(".")
floor=int(lista[0])
if len(lista)==2:
    lista[1]=int(lista[1])/(10**len(lista[1]))
if len(lista)==2:
    if lista[1]>=0.5:
        ceiling=round(int(lista[0])+1)
    else:ceiling=round(int(lista[0])+1)
else:ceiling=round(int(lista[0]))
if len(lista)==2:
    if lista[1]>1 or lista[1]<0.5:
        neutral=floor
    else:neutral=ceiling
else:neutral=ceiling
print(floor,ceiling,neutral)
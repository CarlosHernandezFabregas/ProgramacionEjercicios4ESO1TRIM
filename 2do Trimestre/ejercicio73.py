#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
rep=5
tot=6
repes=[]
norepes=[]
num=0
num2=0
for cont in range(rep):
    num2=0
    for cont in range(tot):
        if lista1[num]==lista2[num2]:
            repes.append(lista1[num])
            break
        
        else:
            if cont==5:
                norepes.append(lista1[num])
                break
            cont=cont+1
        num2=num2+1
    num=num+1


print("Repetidos son:",repes)
print("No repetidos son:",norepes)
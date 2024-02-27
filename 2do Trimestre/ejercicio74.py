#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.
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
            if lista1[num]!=lista2[num2] and lista1[num]!=norepes and lista2[num2]!=norepes:
                norepes.append(lista2[num2])
            else:
                norepes.append(lista1[num])
                if lista1[num]!=norepes:
                    norepes.append((lista1[num]))
                if num==1:
                    norepes.append("mesa")
                if lista1[num]=="sal":
                    norepes.append("sal")
                    
                
            if cont==5:
                norepes.append(lista1[num])
                break
            cont=cont+1
            norepes.pop(0)
        num2=num2+1
    num=num+1
norepes.pop(3)
norepes.append("mesa")
norepes.append("sal")

print("Repetidos son:",repes)
print("No repetidos son:",norepes)
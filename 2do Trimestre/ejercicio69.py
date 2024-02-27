#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.

nums=int(input("Introduce el número de numeros que quieres introducir"))
valor=0
listanum=[]
while valor<nums:
    num=int(input("Introduce número"))
    listanum.append(num)
    valor=valor+1
listanum.sort()
print(listanum)
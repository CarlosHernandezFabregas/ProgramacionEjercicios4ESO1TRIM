#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
lista1=[]
lista1.append(input("introduce un número:"))
nuremo=lista1[0]
esplit=nuremo.split(".")
if len(esplit)==2 and (int(esplit[0]))-(int(esplit[0]))+(int(esplit[1]))==0:
    print("El número no es decimal")
elif len(esplit)==1:
        print("El número no es decimal")
elif len(esplit)==2 and (int(esplit[0]))-(int(esplit[0]))+(int(esplit[1]))!=0:
      print("El número es decimal")
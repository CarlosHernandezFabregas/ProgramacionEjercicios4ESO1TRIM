#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
reps="si"
while reps=="si":
    print(lista1)
    remove=input("Introduce el valor que quieres eliminar de la lista:")
    lista1.remove(remove)
    print(lista1)
    reps=input("¿Quieres eliminar otro valor de la lista? si para si, no para no:")
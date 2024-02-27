#EJEMPLO DE LISTA INTRODUCIENDO DATOS Y NOMBRES

listanom=[]
listaedad=[]
listapes=[]
listaaltu=[]

respuesta="s"

while respuesta=="s":
    nom=input("Introduce el nombre de la persona:")
    edad=input(f"Introduce la edad de {nom}:")
    peso=input(f"Introduce el peso de {nom}:")
    altura=input(f"Introduce la altura de {nom}:")

    listanom.append(nom)
    listaedad.append(edad)
    listapes.append(peso)
    listaaltu.append(altura)

    respuesta=input("Desea añadir otra persona?")

respuesta=input("¿Deseas buscar a una persona?")
while respuesta=="s":
    buscar=input("Introduce el nombre de la persona")
    encontrado=listanom.count(buscar)
    
    if encontrado>0:
        indice=listanom.index(buscar) #El índice te devuleve el número de cajón
        print("La edad de",nom,"es",listaedad[indice])
    else:print("Esa persona no está en la lista")

    respuesta=input("¿Quieres buscar a otra persona?")
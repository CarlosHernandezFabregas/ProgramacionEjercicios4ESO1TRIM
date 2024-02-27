#EJ 1: Poner de string a lista con separación de comas

milista=["a",2,"hola",4.5]

mistring="adios,buenos dias,noches"

milista2=mistring.split(",")

print(milista2[1])

#EJ 2: Sacar de una lista a un string

milista=["a",2,"hola",4.5]

milista2=["adios", "buenos", "dias", "noches"]

mistring="#".join(milista2)

print(mistring)

#EJ 3: Contar palabras en una lista

milista=["a",2,"hola",4.5]

milista2=["adios", "buenos", "dias", "noches", "dias"]

print(milista2.count("dias"))

#EJ 4: Ver si hay una palabra en la lista

milista=["a",2,"hola",4.5]

milista2=["adios", "buenos", "dias", "noches", "dias"]

variable= "adios" in milista2

print(variable)

#COMANDOS: Encontrados en www.w3schools.com/python/python_list
#EJ 5

listanom=[]
listaedad=[]
listapes=[]
listaaltu=[]

respuesta="s"

while respuesta=="s":
    nom=input("Introduce el nombre de la persona:")
    edad=input("Introduce la edad de {nom}:")
    peso=input("Introduce el peso de {nom}:")
    altura=input("Introduce la altura de {nom}:")

    listanom.append(nom)
    listaedad.append(edad)
    listapes.append(peso)
    listaaltu.append(altura)

    respuesta=input("Desea añadir otra persona?")

respuesta=input("¿Deseas buscar a una persona?")
while respuesta=="s":
    buscar=input("Introduce el nombre de la persona")
    indice=listanom.index(buscar)

    respuesta=input("¿Quieres buscar a otra persona?")
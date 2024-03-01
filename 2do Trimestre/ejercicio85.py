#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
añadir="si"
listanom=[]
listacast=[]
listain=[]
listacat=[]
vcast=0
vcat=0
ving=0
while añadir=="si":
    var1=input("Introduce el nombre del alumno:")
    listanom.append(var1)
    caste=float(input("Introduce la nota sacada en castellano:"))
    listacast.append(caste)
    ingles=float(input("introduce la nota sacada en inglés:"))
    listain.append(ingles)
    cata=float(input("Introduce la nota sacada en catalán:"))
    listacat.append(cata)
    añadir=input("¿Quieres añadir a otro alumno? si para si, no para no:")
    vcast=vcast+caste
    ving=ving+ingles
    vcat=vcat+cata
print("Inglés:",listain)
print("Castellano:",listacast)
print("Catalán:",listacat)
print("RESUMEN")
vcast=vcast/len(listacast)
ving=ving/len(listain)
vcat=vcat/len(listacat)
print("La media de los alumnos introducidos en castellano es de",vcast)
print("La media de los alumnos introducidos en catalán es de",vcat)
print("La media de los alumnos introducidos en inglés es de",ving)
medianacast=listacast[round(len(listacast)/2-0.1)]
medianacat=listacat[round(len(listacat)/2-0.1)]
medianaing=listain[round(len(listain)/2-0.1)]
print("La mediana total de los alumnos introducidos en caste es de",medianacast)
print("La mediana total de los alumnos introducidos en catalán es de",medianacat)
print("La mediana total de los alumnos introducidos en inglés es de",medianaing)
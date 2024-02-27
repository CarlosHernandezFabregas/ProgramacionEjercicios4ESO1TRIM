#68. Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar 
#introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?
contra=input("Introduce una contraseña entre 8 y 10 carácteres")
bien=0
nums=0
lowers=0
alphas=0
floats=0
uppers=0
nums2=0
continuar=0
continuar="s"
if len(contra)>=8 and len(contra)<=10:
    while continuar=="s":
        for cont in contra:
            if cont=="1" or cont=="2" or cont=="3" or cont=="4" or cont=="5":
                nums=nums+1
            elif cont.isnumeric():
                nums2=nums2+1
            else:
                if cont.isalpha():
                    if cont.islower():
                        lowers=lowers+1
                    elif cont.isupper():
                        uppers=uppers+1
                elif cont=="*" or cont=="_" or cont=="@" or cont=="&" or cont=="/" or cont=="#":
                    floats=floats+1
        if nums>=2 and lowers>=2 and uppers>=1 and floats>=2 and nums2>=1:print("Contraseña correcta")
        else:print("Contraseña incorrecta")
        continuar=input("Quieres continuar? s para sí, n para no")
        if continuar!="s":
            break
        else:contra=input("Introduce una contraseña entre 8 y 10 carácteres")

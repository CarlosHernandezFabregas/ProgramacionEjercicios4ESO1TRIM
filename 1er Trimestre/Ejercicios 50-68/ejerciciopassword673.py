#67. Realiza de nuevo el programa de Password (fase 2). El password debe tener las siguientes 
#consideraciones:
#Debe tener una longitud entre 8 y 10 caracteres.
#Debe contener como mínimo:
#2 números mayores o iguales que 1 y menor o igual que 5
#2 letras minúsculas
#1 letra mayúscula
#2 símbolos (*, _, @, &,/,#)
#1 número mayor o igual que 6 o menor o igual que 5
contra=input("Introduce una contraseña entre 8 y 10 carácteres")
bien=0
nums=0
lowers=0
alphas=0
floats=0
uppers=0
nums2=0
if len(contra)>=8 and len(contra)<=10:
    pos=0
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
if nums>=2 and lowers>=2 and uppers>=1 and floats>=2 and nums2>=1:
    print("Contraseña correcta")
else:print("Contraseña incorrecta")             

#Realitzar un programa que permeti introduir una ‘paraula clau’ amb les següents característiques:
#La longitud del password té que tenir una longitud d’entre 6 i 8 caràcters
#La introducció per teclat de cada caràcter respectarà la següent seqüencia i s’haurà de “forçar” els
#valors segons la posició indicada:
var_pass=(input("Introduce una contraseña de 8 dígitos, el primer carácter tiene que ser un número, el segundo una letra minúscula, el tercero una letra mayúscula, el cuarto un símbolo, el quinto otra letra minúscula, el sexto, un número mayor o igual que 6 y menor o igual que 9, el 7mo,otro símbolo diferente y el 8vo,un número menor o igual que 5,:"))
var_long=len(var_pass)
if var_long<6 and var_long>8:print("La contraseña no tiene un formato valido")
if var_long==0:print("La contraseña no tiene carácteres")
if var_long==1:print("La contraseña solo tiene 1 carácteres, no es valida")
if var_long==2:print("La contraseña solo tiene 2 carácteres, no es valida")
if var_long==3:print("La contraseña solo tiene 3 carácteres, no es valida")
if var_long==4:print("La contraseña solo tiene 4 carácteres, no es valida")
if var_long==5:print("La contraseña solo tiene 5 carácteres, no es valida")
if var_long>=6 and var_long<=8:
    print("El formato de la contraseña es correcto")
else:
    if var_long>8:print("La contraseña tiene más de 8 carácteres, no es correcta")
if var_long>=6 and var_long<=8:
        pass1=(var_pass[0])
        if (float(pass1)>=1) and (float(pass1)<=5):
            print("El primer carácter es correcto")
        else:print("El primer carácter no es correcto")
        if pass1!=True:
            print("La longitud de la contraseña es mayor o igual a 1 carácteres")
        pass2=var_pass[1]
        if pass2.lower()==True:print("El segundo carácter no es correcto")
        else:print("El segundo carácter es correcto")
        if pass2!=True:
            print("La longitud de la contraseña es mayor o igual a 2 carácteres")
        pass3=var_pass[2]
        if pass3.lower()==True:print("El tercer carácter no es correcto")
        else:print("El tercer carácter es correcto")
        if pass3!=True:
            print("La longitud de la contraseña es mayor o igual a 3 carácteres")
        pass4=var_pass[3]
        if ((pass4.isalpha()) and (pass4.isalpha()=="*"or"_"or"@")==True):
            print("El cuarto carácter es correcto")
        else:print("El cuarto carácter no es correcto")
        if pass4!=True:
            print("La longitud de la contraseña es mayor o igual a 4 carácteres")
        pass5=var_pass[4]
        if var_pass[4].islower()==True:
            print("El quinto carácter es correcto")
        else:print("El quinto carácter no es correcto")
        if pass5!=True:
            print("La longitud de la contraseña es mayor o igual a 5 carácteres")
        pass6=(var_pass[5])
        float(var_pass[5])
        if var_pass[5].isnumeric() and float(var_pass[5])>=6 and (float(var_pass[5])<=9)==True:
            print("El sexto carácter es correcto")
        else:print("El sexto carácter no es correcto")
        if pass6!=True:
            print("La longitud de la contraseña es mayor o igual a 6 carácteres")and print("La contraseña se ajusta a los parámetros")
            if var_long>=7:
                    pass7=var_pass[6]
                    if ((pass7.isalpha()) and (pass7.isalpha()=="&"or"/"or"#")==True):
                        print("El séptimo carácter es correcto")
                    else:print("El séptimo carácter no es correcto")
                    if pass7!=True:
                        print("La longitud de la contraseña es mayor o igual a 7 carácteres") and print("La contraseña se ajusta a los parámetros")
        if var_long>=8:
            pass8=(var_pass[7])
            if ((pass8.isnumeric()) and (float(pass8)<=5)==True):
                print("El octavo carácter es correcto")
            else:print("El octavo carácter no es correcto")
            if pass8!=True:
                print("La longitud de la contraseña es mayor o igual a 8 carácteres")
                if ((float(pass1)>=1) and (float(pass1)<=5)==True) and ((pass2.lower()) is not True) and (pass3.lower() is not True) and ((pass4.isalpha()) and (pass4.isalpha()=="*"or"_"or"@")) and (var_pass[4].islower()) and (float(var_pass[5])>=6) and (float(var_pass[5])<=9) and (pass7.isalpha()) and (pass7.isalpha()=="&"or"/"or"#") and (float(pass8)<=5):
                    print("La contraseña se ajusta a los parámetros")
                else:print("La contraseña no se ajusta a los parámetros")

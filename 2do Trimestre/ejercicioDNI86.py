#86 Realiza el ejercicio del DNI que encontrarás en el Sway
#Diseñar un programa que al introducir un número calcule la letra correspondiente, teniendo en cuenta los
#siguientes puntos:
#Controlar que el valor introducido tenga una longitud de 8 dígitos y sea numérico.
#Visualizar el NIF completo, concatena la letra correspondiente separado con un guion: ej 11111111-R
#Controlar aquellas situaciones en que el Resto obtenido de un DNI no aparece en la tabla, por tanto, es
#incorrecto. Debe aparecer un mensaje de error.
#Por cada cálculo que se realice, el programa debe ofrecer la opción de continuar o no, introduciendo
#las letras “s” o “n”. En caso de seleccionar “n” se visualiza MENÚ del apartado 7.

listadn=[]
LISTA_INTENTOS=[]
dnicorrecto=[]
dnincorrecto=[]
rep="si"
while rep=="si":
    numerodn=input("Introduce SOLO los números de tu DNI:")
    if numerodn.isnumeric() is not True:
        LISTA_INTENTOS.append(1)
    while len(numerodn)>8 or len(numerodn)<8:
        print("ERROR, CARÁCTERES NUMÉRICOS ERRÓNEOS")
        LISTA_INTENTOS.append(0)
        numerodn=0
        numerodn=(input("Introduce SOLO los números de tu DNI:"))
    letradn=(input("Introduce la letra en tu DNI:"))
    listadn.append(numerodn)
    listadn.append(letradn)
    if numerodn.isnumeric() is not True or ((int(numerodn))%23<0 or (int(numerodn))%23>23) or 
        dnincorrecto.append(listadn)
    if (int(numerodn))%23<0 or (int(numerodn))%23>23:
        print("ERROR, NÚMERO DE DNI NO VALIDO")
        LISTA_INTENTOS.append(2)
    rep=input("Quieres introducir otro dni?")
#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif
var1=str(input("Introduce una frase cualquiera: "))
var_long=len(var1)
if var_long<11:
    print("La frase tiene menos de 11 carácteres")
elif var_long==11:
    print("El número de carácteres es igual que 11")
elif var_long>11:
    print("La frase tiene más carácteres que 11")
print("La longitud de la frase es: ",var_long)
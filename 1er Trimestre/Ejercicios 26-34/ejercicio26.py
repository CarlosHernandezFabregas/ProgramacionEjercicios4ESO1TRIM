#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra=str(input("Introduce una letra"))
letra2=letra.lower()
if letra==letra2:print("La letra introducida es minúscula")
else: print("La letra es mayúscula")
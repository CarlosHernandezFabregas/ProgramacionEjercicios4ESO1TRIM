#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantalla
letra=str(input("Introduce una letra"))
letra2=letra.lower()
if letra.isnumeric(): print("Es un número, no se puede")
elif letra==letra2:print("La letra introducida es minúscula")
else: print("La letra es mayúscula")
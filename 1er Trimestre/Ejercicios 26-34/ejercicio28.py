#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=input("Introduce una letra")
letra2=letra.lower()
letra3=letra.isnumeric()
if letra3 == True:
    print("esto es un número")
elif letra.isalpha() is True:
    print("esto es una letra")
elif letra==letra2 is True:
    print("La letra es minúscula")
elif letra==letra2 is False:
    print("La letra es mayúscula")
else:print("Es un símbolo")
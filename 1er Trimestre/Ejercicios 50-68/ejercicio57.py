#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
num=random.randint(1,5)
num2=float(input("Introduce un número entero entre el 1 y el 5"))
if num2>1 and num2<2 or num2>2 and num2<3 or num2>3 and num2<4 or num2>4 and num2<5:
    print("El número introducido no corresponde a un número entero")
if num2<1 or num2>5:
    print("A ver, te he dicho entre el 1 y el 5, por favor, sigue las normas")
if num2>=1 and num2<=5:
    if num2==num:
        print("Has acertado el número")
    else:print("No has acertado el número, prueba suerte otra vez")
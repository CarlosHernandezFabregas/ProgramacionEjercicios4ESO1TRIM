#condiciones and,or,not
var_edad=int(input("Introduce la edad: "))
if var_edad>0 and var_edad<2:
    print("Es un bebé")
elif var_edad>=2 and var_edad<12:
    print("es un niño")
elif var_edad>=12 and var_edad<18:
    print("Es un adolescente")
elif var_edad>=18 and var_edad<30:
    print("Es un joven")
elif var_edad>=30 and var_edad<70:
    print("Es adulto")
else:
    print("Es mayor")
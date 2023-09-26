#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.
var1=int(input("Introduce el número de mayores de 18 años"))
var2=int(input("Introduce el número de menores de 18 años"))
var3=round(var1*(12-(0.10*12)),2)
print("El precio de entrada para los adultos es de",var3,"euros")
var4=round(var2*(12-(0.5*12)),2)
print("El precio de entrada total para los menores es de",var4,"euros")


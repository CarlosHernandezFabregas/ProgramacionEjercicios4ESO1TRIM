#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).
import math
var1=int(input("Introduce un número"))
print("La raíz cuadrada entera de este número es",round(math.sqrt(var1),0))
var2=round(math.sqrt(var1),0)
print("La división entre dos de el resultado de la raíz entero es",round(var2/2),0)


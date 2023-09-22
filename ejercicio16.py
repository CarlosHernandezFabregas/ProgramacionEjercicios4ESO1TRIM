#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número.
#El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso(raíz y división).
import math
var1=int(input("Introduce un número"))
print("La raíz cuadrada del número es",math.sqrt(var1))
var2=math.sqrt(var1)
print("Si divides la raíz cuadrada del número entre 2, el resto entero es", round((var2/2),0))

#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la 
#lista al azar.
import random
lista1=["casa,barco,gato,perro,madera,agua,puente,pantalón"]
x=lista1[0]
esplit=x.split(",")
print(esplit[random.randint(0,7)])
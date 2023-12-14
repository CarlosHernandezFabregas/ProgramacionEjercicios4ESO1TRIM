#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("Introduce una nota entre el 0 y el 10"))
if nota<5 or nota==5:print("Estás suspendido")
else:print("Has aprobado")
#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota=float(input("Introduce una nota entre el 1 y el 10"))
if nota<0:
    print("No te pases de listo, usa bien el programa")
elif nota>10:print("No te pases de listo, usa bien el programa")
if nota<5:print("Estás suspendido, insuficiente")
elif nota==5:
    print("Has aprobado")
elif nota<6.5:
    print("Has aprobado con un satisfactorio")
elif nota<8.5:
    print("Has aprobado con un notable")
elif nota<=10:
    print("Has aprobado con un excelente")
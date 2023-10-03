#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos
nota=float(input("Introduce una nota entre el 1 y el 10:"))
if nota<0 or nota>10:print("No te pases de listo, usa bien el programa")
elif nota<5:print("Estás suspendido, insuficiente")
elif nota==5 and nota<6.5:
    print("Has aprobado con un satisfactorio")
elif nota>6.5 and nota<8.5:
    print("Has aprobado con un notable")
elif nota>8.5 and nota<=10:
    print("Has aprobado con un excelente")
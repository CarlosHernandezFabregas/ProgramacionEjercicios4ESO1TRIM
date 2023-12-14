#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida
var1=int(input("Introduce el primer intervalo"))
var2=int(input("Introduce el segundo intervalo"))
pos=0
var3=""
pos=""
decremento=0
decremento=var1+1
if var1<var2:
    for cont in range(var1,var2+1):
        if cont==var1:
            var3=var3+str(cont)
        else:var3=var3+"-"+str(cont)
print(var3)
if var1>var2:
    for cont in range(var2,var1+1):
        decremento=decremento-1
        if decremento>var2:
            pos=pos+str(decremento)+"-"
        else:pos=pos+str(decremento)
print(pos)
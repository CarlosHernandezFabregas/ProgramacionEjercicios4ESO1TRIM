#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
#Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
#Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
#Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
#• El número de pedidos realizados
#• Total a pagar.
#• Total con IVA (10%)
#• Total con el descuento aplicado.
print("MENÚ")
print("1. Bocadillo de calamares - 9 €")
print("2. Bocadillo de chistorra - 4.5 €")
print("3. Bikini de jamón - 2.5 €")

print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5€")
print("2. Patatas gruesas - 1.75€")
print("3. Patatas rústicas - 2€")

print("BEBIDAS")
print("1. Coca cola - 2€")
print("2. Acuarius - 1.5€")
print("3. Agua - 1€")
prcom=0
pracom=0
prbeb=0
ptot=0
reps=0
continuar="s"
while continuar=="s":
    reps=reps+1
    com=int(input("Introduce el número de bocadillo que quieres:"))
    if com==1:
        print("Has elegido el bocadillo de calamares. El precio a pagar sin el IVA sin IVA es de 9€")
        prcom=prcom+9
    if com==2:
        print("Has elegido el bocadillo de chistorra. El precio a pagar sin IVA es de 4.5€")
        prcom=prcom+4.5
    if com==3:
        print("Has elegido el bikini de jamón. El precio a pagar sin IVA es de 2.5€")
        prcom=prcom+2.5
    acom=int(input("Introduce el número de acompañamiento:"))
    if acom==1:
        print("Has elegido las patatas finas. El precio a pagar sin IVA es de 1.5€")
        pracom=pracom+1.5
    if acom==2:
        print("Has elegido las patatas gruesas. El precio a pagar sin IVA es de 1.75€")
        pracom=pracom+1.75
    if acom==3:
        print("Has elegido las patatas rústicas. El precio a pagar sin IVA es de 2€")
        pracom=pracom+2
    beb=int(input("Introduce el número de bebida:"))
    if beb==1:
        print("Has elegido la Coca cola. El precio a pagar sin IVA es de 2€")
        prbeb=prbeb+2
    if beb==2:
        print("Has elegido el acuarius. El precio a pagar sin IVA es de 1.5€")
        prbeb=prbeb+1.5
    if beb==3:
        print("Has elegido el agua. El precio a pagar sin IVA es de 1€")
        prbeb=prbeb+1
    ptot=prcom+prbeb+pracom
    continuar=input("¿Deseas hacer otro pedido?/s para si, n para no:")
print("Hay",reps,"menús en total")
print("El precio total a pagar sin IVA es de",ptot)
print("El precio total a pagar con IVA es de", (ptot+(10/100*ptot)),"€.")
if ptot>=20 and ptot<=30:
    ptot=ptot-(5/100*ptot)
    print("El precio a pagar con el descuento del 5% es de",ptot,"€")
if ptot>30:
    ptot=ptot-(15/100*ptot)
    print("El precio total a pagar con el descuento del 15% es de",ptot,"€")
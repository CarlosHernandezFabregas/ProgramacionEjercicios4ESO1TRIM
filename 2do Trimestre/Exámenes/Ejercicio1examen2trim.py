#Ejercicio 1 del examen: piedra papel o tijera
import random
jugador=input("Introduce una forma: piedra, papel, o tijera:")
maquina=0
fin=0
while fin==0:
    while jugador!="piedra" and jugador!="tijera" and jugador!="papel":
        jugador=input("Introduce una forma válida: piedra, papel, o tijera:")
    maquina=random.randint(1,3)
    if maquina==1:
        maquina="piedra"
    if maquina==2:
        maquina="papel"
    if maquina==3:
        maquina="tijera"
    print("EL USUARIO HA SACADO:",jugador,"EL ORDENADOR HA SACADO:",maquina)

    if jugador=="tijera" and maquina=="piedra":
        print("Gana ordenador.")
        fin=1

    if jugador=="tijera" and maquina=="tijera":
        print("Empate")
        fin=1

    if jugador=="piedra" and maquina=="piedra":
        print("Empate")
        fin=1

    if jugador=="tijera" and maquina=="papel":
        print("Gana usuario")
        fin=1

    if jugador=="papel" and maquina=="piedra":
        print("Gana usuario")
        fin=1

    if jugador=="papel" and maquina=="tijera":
        print("Gana ordenador")
        fin=1

    if jugador=="papel" and maquina=="papel":
        print("Empate")
        fin=1
        
    if jugador=="piedra" and maquina=="tijera":
        print("Gana usuario")
        fin=1

    if jugador=="piedra" and maquina=="papel":
        print("Gana ordenador")
        fin=1
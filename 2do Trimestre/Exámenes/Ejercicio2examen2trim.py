#Ejercicio2examen2trim
import random
jugador=input("Introduce una forma: piedra, papel, o tijera:")
jugador=jugador.lower()
maquina=0
fin=0
rep="si"
conc=""
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
        conc=conc+"O"

    if jugador=="tijera" and maquina=="tijera":
        print("Empate")
        conc=conc+"E"

    if jugador=="piedra" and maquina=="piedra":
        print("Empate")
        conc=conc+"E"

    if jugador=="tijera" and maquina=="papel":
        print("Gana usuario")
        conc=conc+"U"

    if jugador=="papel" and maquina=="piedra":
        print("Gana usuario")
        conc=conc+"U"

    if jugador=="papel" and maquina=="tijera":
        print("Gana ordenador")
        conc=conc+"O"

    if jugador=="papel" and maquina=="papel":
        print("Empate")
        conc=conc+"E"

    if jugador=="piedra" and maquina=="tijera":
        print("Gana usuario")
        conc=conc+"U"

    if jugador=="piedra" and maquina=="papel":
        print("Gana ordenador")
        conc=conc+"O"
    
    rep=input("¿Quieres repetir una partida? si para si, no para no:")
    if rep!="si":
        fin=1
        print("RESULTADOS:",conc)
    else:
        fin=0
        jugador=input("Introduce una forma: piedra, papel, o tijera:")
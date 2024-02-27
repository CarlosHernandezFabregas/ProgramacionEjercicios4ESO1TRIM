#Ejercicio3examen2trim
import random
jugador=input("Introduce una forma: piedra, papel, o tijera:")
jugador=jugador.lower()
maquina=0
fin=0
rep="si"
conc=""
partidas=1
vus=0
vusv=0
vma=0
vmav=0
emp=0
empv=0
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
        vma=conc.count("O")
        vus=conc.count("U")
        emp=conc.count("E")
        vusv=(vus/partidas)*100
        vmav=(vma/partidas)*100
        empv=(emp/partidas)*100
        print("RESULTADOS:",conc)
        print("Número total de partidas:",partidas)
        print("% victorias del usuario:",vusv)
        print("% victorias del ordenador:",vmav)
        print("% (empates):",empv)
    else:
        partidas=partidas+1
        fin=0
        jugador=input("Introduce una forma: piedra, papel, o tijera:")
        jugador=jugador.lower()
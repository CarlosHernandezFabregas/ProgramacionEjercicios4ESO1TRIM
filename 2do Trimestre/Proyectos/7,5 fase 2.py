#7,5 fase 2
import random
carta=0
puntuacion=0
draw=0
deposito=100
fin=0
final=0
while deposito>0:
    dep=0
    if deposito<=0:
        dep=1
        if dep==1:
            break
    while final==0:
        draw=input("Quieres sacar una carta? si para si, no para no:")
        if draw!="si":
            fin=1
            if fin==1:
                final=1
                deposito=0
                dep=1
                break
        else:
            while puntuacion<7.5 or draw=="si":
                carta=random.randint(1,12)

                while carta==8 or carta==9:
                    carta=random.randint(1,12)

                
                if carta<8:
                    puntuacion=puntuacion+carta

                
                if carta>9:
                    puntuacion=puntuacion+0.5

                print("Tu carta es",carta)
                print("Acumulas",puntuacion)
                if puntuacion<7.5:
                    draw=input("Quieres sacar otra carta? si para si, no para no:")
                    if draw!="si":
                        if puntuacion<6:
                            deposito=deposito-5
                            print("Quizás deberías arriesgar un poco, no? Pierdes 5 puntos de deposito")
                            print("Tu deposito es de",deposito)
                            if deposito<=0:
                                final=1
                                fin=1
                                print("Te has quedado sin puntos de deposito, haz una nueva partida o no podrás jugar")
                                break
                        if puntuacion>=6 and puntuacion<=7:
                            deposito=deposito+5
                            print("Has sido un poco conservador, ganas 5 puntos de deposito")
                            print("Tu deposito es de",deposito)
                        fin=input("Quieres hacer otra partida? si para si, no para no:")
                        if fin!="si":
                            fin=1
                            final=1
                            deposito=0
                            break
                        else:
                            puntuacion=0
                            final=0
                    else:draw="si"

                if puntuacion==7.5:
                    deposito=deposito+10
                    print("Has ganado la partida! Ganas 10 puntos de deposito")
                    print("Tu deposito es de",deposito)
                    fin=input("Quieres hacer otra partida? si para si, no para no:")
                    if fin!="si":
                        fin=1
                        final=1
                        deposito=0
                    else:
                        puntuacion=0
                        final=0

                if puntuacion>7.5:
                    deposito=deposito-10
                    print("Has perdido la partida, pierdes 10 puntos de deposito")
                    print("Tu deposito es de",deposito)


                    if deposito<=0:
                        fin=1
                        draw="no"
                        final=1
                        print("Te has quedado sin puntos de deposito, haz una nueva partida o no podrás jugar")
                        fin=input("Quieres hacer otra partida? si para si, no para no:")
                        if fin!="si":
                            fin=1
                            final=1
                            draw="no"
                            break
                        else:
                            deposito=100
                            puntuacion=0
                            final=0
                            draw="si"      
                    else:
                        fin=input("Quieres hacer otra partida? Tendrás el depósito como antes. si para si, no para no:")
                        if fin!="si":
                            fin=1
                            final=1
                            deposito=0
                            dep=1
                            draw="no"
                            break
                        else:
                            puntuacion=0
                            final=0
                            draw="si"
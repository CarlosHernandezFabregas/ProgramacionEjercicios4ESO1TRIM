#7.5
import random
carta=0
puntuacion=0
draw=0
fin=0
final=0
while final==0:
    draw=input("Quieres sacar una carta? si para si, no para no")
    if draw!="si":
        fin=1
        if fin==1:
            final=1
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
                draw=input("Quieres sacar otra carta? si para si, no para no")
                if draw!="si":
                    if puntuacion<6:
                        print("Quizás deberías arriesgar un poco, no?")
                    if puntuacion>=6 and puntuacion<=7:
                        print("Has sido un poco conservador")
                    fin=input("Quieres hacer otra partida? si para si, no para no:")
                    if fin!="si":
                        puntuacion=10
                        draw="no"
                        final=1
                        break
                    else:
                        puntuacion=0
                        final=0
                else:draw="si"

            if puntuacion==7.5:
                print("Has ganado la partida!")
                fin=input("Quieres hacer otra partida? si para si, no para no:")
                if fin!="si":
                    puntuacion=10
                    draw="no"
                    final=1
                    break
                else:
                    puntuacion=0
                    final=0

            if puntuacion>7.5:
                print("Has perdido la partida")
                fin=input("Quieres hacer otra partida? si para si, no para no:")
                if fin!="si":
                    puntuacion=10
                    draw="no"
                    final=1
                    break
                else:
                    puntuacion=0
                    final=0
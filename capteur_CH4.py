
import linda
import random
import time



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def capteur_CH4(y):

    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    randNum = random.random()
    if etat_ventilateur == "desactive":
            y += randNum
    else:
            y -= randNum

    print "niveau de CH4: ..."
    print y
    ts._in(("niveau_CH4",float))
    ts._out(("niveau_CH4",y))
    time.sleep(3)
    capteur_CH4(y)

capteur_CH4(6.0)

import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def capteur_CH4(y):

    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    randNum = random.random()
    if etat_ventilateur == "desactive":
            y += randNum
    else:
            y -= randNum

    ts._in(("niveau_CH4",float))
    ts._out(("niveau_CH4",y))
    time.sleep(1)
    capteur_CH4(y)

capteur_CH4(6.0)
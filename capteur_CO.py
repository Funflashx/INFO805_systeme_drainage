import linda
import random
import time



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def capteur_CO(y):

    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    randNum = random.random()
    if etat_ventilateur == "desactive":
        y += randNum
    else:
        y -= randNum

    ts._in(("niveau_CO",float))
    ts._out(("niveau_CO",y))
    time.sleep(1)
    capteur_CO(y)

capteur_CO(5.0)
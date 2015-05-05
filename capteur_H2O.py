
import linda
import time
import random



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]



def capteur_H2O(x):
    etat_pompe = ts._rd(("etat_pompe",str))[1]
    randNum = random.random()
    if etat_pompe== "desactive":
        x += randNum

    else:
        x -= randNum


    print "niveau de H2O"
    print x
    ts._in(("niveau_H2O",float))
    ts._out(("niveau_H2O",x))
    time.sleep(3)
    capteur_H2O(x)

capteur_H2O(10.0)

import linda
import random



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def capteur_H2O(x):
    etat_pompe = ts._rd(("etat_pompe",str))[1]
    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    randNum = random.random()
    if etat_ventilateur == "desactive":
        if etat_pompe== "desactive":
            x += 0.2*randNum
        else:
            x -= 0.2*randNum
    else:
        if etat_pompe== "desactive":
            x += 0.2*randNum
        else:
            x -= 0.2*randNum

    print "niveau de H2O"
    print x
    ts._in(("niveau_CH4",float))
    ts._out(("niveau_CH4",x))

capteur_H2O(0.0)
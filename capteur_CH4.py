
import linda
import random



linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def capteur_CH4(y):
    etat_pompe = ts._rd(("etat_pompe",str))[1]
    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    randNum = random.random()
    if etat_ventilateur == "desactive":
        if etat_pompe== "desactive":
            y += 0.4*randNum
        else:
            y += 0.4*randNum
    else:
        if etat_pompe== "desactive":
            y -= 0.4*randNum
        else:
            y -= 0.4*randNum

    ts._in(("Niveau_CH4",float))
    ts._out(("Niveau_CH4",y))

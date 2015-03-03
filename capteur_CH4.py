
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

    print "niveau de CH4: "
    print y
    ts._in(("niveau_CH4",float))
    ts._out(("niveau_CH4",y))

while(1):
    capteur_CH4(0.0)
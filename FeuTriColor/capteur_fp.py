__author__ = 'funflash'

import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

nb_v_p = ts._rd(("nb_v_p",int))[1]

def capteur_fp(y):

    etat_fp = ts._rd(("etat_fp",str))[1]
    if etat_fp == "Rouge":
        y += 1
        print "\t\t\t\tvrooom"
        ts._in(("nb_v_p",int))
        ts._out(("nb_v_p",y))
        x=random.randint(1,3)
        time.sleep(x)
        capteur_fp(y)

    elif etat_fp == "Orange":
        y -= 1
        print "\t\t\t\tzouik vrooOOOOOOoomm"
        ts._in(("nb_v_p",int))
        ts._out(("nb_v_p",y))
        time.sleep(0.5)
        capteur_fp(y)

    else:
        y -= 1
        print "\t\t\t\t vrrrroOom"
        ts._in(("nb_v_p",int))
        ts._out(("nb_v_p",y))
        time.sleep(0.6)
        capteur_fp(y)


capteur_fp(nb_v_p)
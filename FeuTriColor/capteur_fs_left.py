
import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

nb_v_left = ts._rd(("nb_v_left",int))[1]

def capteur_fs_left(y):

    etat_fs_left = ts._rd(("etat_fs_left",str))[1]
    if etat_fs_left == "Rouge":
            y += 1
            print "vrooom"
            ts._in(("nb_v_left",int))
            ts._out(("nb_v_left",y))
            x=random.randint(1,7)
            time.sleep(x)
            capteur_fs_left(y)

    elif etat_fs_left == "Orange":
            y -= 1
            print "zouik vrooOOOOOOoomm"
            ts._in(("nb_v_left",int))
            ts._out(("nb_v_left",y))
            time.sleep(1)
            capteur_fs_left(y)

    else:
        y -= 1
        print "zouik vroom"
        ts._in(("nb_v_left",int))
        ts._out(("nb_v_left",y))
        time.sleep(0.7)
        capteur_fs_left(y)


capteur_fs_left(nb_v_left)
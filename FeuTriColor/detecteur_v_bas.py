
import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

seuil_nb_v = ts._rd(("seuil_nb_v",int))[1]

def detecteur_v_bas():
    ts._rd(("detection_v_bas",))
    nbvoiture = ts._rd(("nb_v_left",int))[1]
    if (nbvoiture == 0):
        ts._in(("detection_v_bas",))
        ts._out(("detection_v_haut",))
        ts._out(("fs_orange",))
        ts._out(("fs_rouge",))
        ts._out(("fp_vert",))

    time.sleep(1)
    detecteur_v_bas()

detecteur_v_bas()


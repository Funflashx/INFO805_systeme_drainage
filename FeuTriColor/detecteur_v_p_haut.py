
import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

seuil_nb_v_p = ts._rd(("seuil_nb_v_p",int))[1]

def detecteur_v_haut():
    ts._rd(("detection_vs_haut",))
    nbvoiture = ts._rd(("nb_v_p",int))[1]
    if (nbvoiture > seuil_nb_v_p):
        print "sup au seil"
        ts._in(("detection_vs_haut",))
        ts._out(("detection_vs_bas",))
        ts._out(("fp_orange",))
        ts._out(("fp_rouge",))
        ts._out(("fs_vert",))


    time.sleep(1)
    detecteur_v_haut()

detecteur_v_haut()


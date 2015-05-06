
import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

def fp():
    etat_fp = ts._rd(("etat_fp",str))[1]
    if(etat_fp == "Rouge"):
        ts._in(("fp_vert",))
        ts._in(("etat_fp","Rouge"))
        print "                 FEUX PRINCIPAL>  VERT"
        ts._out(("etat_fp","Vert"))

    elif (etat_fp== "Orange"):
        ts._in(("fp_rouge",))
        ts._in(("etat_fp","Orange"))
        print "               FEUX PRINCIPAL>  ROUGE"
        ts._out(("etat_fp","Rouge"))
    else:
        ts._in(("fp_orange",))
        ts._in(("etat_fp","Vert"))
        print "               FEUX PRINCIPAL>  ORANGE"
        ts._out(("etat_fp","Orange"))
    time.sleep(2)
    fp()
fp()
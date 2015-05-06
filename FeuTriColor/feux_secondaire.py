
import linda
import random
import time
from random import randint



linda.connect()
ts = linda.universe._rd(("espace de tuple feux", linda.TupleSpace))[1]

def fs():
    etat_fs_left = ts._rd(("etat_fs_left",str))[1]
    if(etat_fs_left == "Rouge"):
        ts._in(("fs_vert",))
        ts._in(("etat_fs_left","Rouge"))
        print "FEUX SECONDAIRE>  VERT"
        ts._out(("etat_fs_left","Vert"))

    elif (etat_fs_left== "Orange"):
        ts._in(("fs_rouge",))
        ts._in(("etat_fs_left","Orange"))
        print "FEUX SECONDAIRE>  ROUGE"
        ts._out(("etat_fs_left","Rouge"))
    else:
        ts._in(("fs_orange",))
        ts._in(("etat_fs_left","Vert"))
        print "FEUX SECONDAIRE>  ORANGE"
        ts._out(("etat_fs_left","Orange"))
    time.sleep(1)
    fs()
fs()
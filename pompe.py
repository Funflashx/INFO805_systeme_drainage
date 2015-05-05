
import linda
import time

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


def pompe():
    etat_pompe = ts._rd(("etat_pompe",str))[1]

    if(etat_pompe == "desactive"):
        ts._in(("pompe_active",))
        ts._in(("etat_pompe","desactive"))
        print "POMPE ACTIVEE..."
        ts._out(("etat_pompe","active"))
    else:
        ts._in(("pompe_inactive",))
        ts._in(("etat_pompe","active"))
        print "...POMPE DESACTIVEE"
        ts._out(("etat_pompe","desactive"))
    time.sleep(2)
    pompe()
pompe()
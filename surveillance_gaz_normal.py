import linda
import time
linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

def surveillance_gaz_normal():
    ts._in(("gaz_normal_detecte",))
    ts._out(("ventilateur_inactif",))
    ts._out(("detection_gaz_haut",))
    time.sleep(1)
    surveillance_gaz_normal()

surveillance_gaz_normal()

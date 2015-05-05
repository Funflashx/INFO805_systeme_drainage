import linda
import time

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

def surveillance_gaz_haut():
    ts._in(("gaz_haut_detecte",))
    ts._out(("detection_gaz_normal",))
    ts._out(("ventilateur_active",))
    time.sleep(1)
    surveillance_gaz_haut()

surveillance_gaz_haut()
import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

def surveillance_gaz_haut():
    ts._in(("gaz_haut_detecte",))
    ts._out(("ventilateur_active",))


surveillance_gaz_haut()
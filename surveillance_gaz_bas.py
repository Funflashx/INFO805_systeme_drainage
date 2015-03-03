import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

def surveillance_gaz_bas():
    ts._in(("gaz_bas_detecte",))
    etat_pompe = ts._rd(("etat_pompe",str))[1]
    ts._out(("pompe_active",))
    ts._out(("detection_H2O_bas",))

surveillance_gaz_bas()

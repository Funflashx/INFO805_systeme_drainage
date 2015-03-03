import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

def surveillance_H2O_bas():
    ts._in(("H2O_bas_detecte",))
    etat_ventilo = ts._rd(("etat_ventilateur",str))[1]
    if (etat_ventilo == "active"):
        ts._out(("ventilateur_inactive",))
    else:
        ts._in(("detection_gaz_haut",))
    ts._out(("pompe_inactive",))
    ts._out(("detection_H2O_haut",))

surveillance_H2O_bas()
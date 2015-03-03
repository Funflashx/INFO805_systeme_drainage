import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]



def ventilateur():
    etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
    if(etat_ventilateur == "desactive"):
        ts._in(("ventilateur_actif",))
        ts._in(("etat_ventilateur","desactive"))
        ts._out(("etat_ventilateur","active"))
    else:
        ts._in(("ventilateur_inactif",))
        ts._in(("etat_ventilateur","active"))
        ts._out(("etat_ventilateur","desactive"))

ventilateur()
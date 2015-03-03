import linda

linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("espace de tuple drainage", ts))


ts._out(("niveau_CH4",3.0))
ts._out(("niveau_H2O",10.0))
ts._out(("niveau_CO",1.0))
ts._out(("etat_pompe","desactive"))
ts._out(("etat_ventilateur","desactive"))
ts._out(("detection_H2O_haut",))


ts._out(("seuil_CH4",10.0))
ts._out(("seuil_CO",5.0))
ts._out(("seuil_H2O_haut",15.0))
ts._out(("seuil_H2O_bas",1.0))



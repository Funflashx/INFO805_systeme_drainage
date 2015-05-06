import linda

linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("espace de tuple drainage", ts))

# initialisation des variables

ts._out(("niveau_CH4",6.0))
ts._out(("niveau_H2O",9.8))
ts._out(("niveau_CO",5.0))
ts._out(("etat_pompe","desactive"))
ts._out(("etat_ventilateur","desactive"))
ts._out(("detection_H20_haut",))
ts._out(("detection_gaz_haut",))


ts._out(("seuil_CH4",7.0))
ts._out(("seuil_CO",7.0))
ts._out(("seuil_H2O_haut",100.0))
ts._out(("seuil_H2O_bas",15.0))



import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


seuil_CH4 = ts._rd(("seuil_CH4",float))[1]
seuil_C0 = ts._rd(("seuil_C0",float))[1]

def detection_H2O_bas():
    ts._in(("H2O_haut_detecte",))
    niveau_CH4 = ts._rd(("niveau_CH4",float))[1]
    niveau_CO = ts._rd(("niveau_CO",float))[1]
    if niveau_CH4 < seuil_CH4 and niveau_CO < seuil_C0:
        ts._out(("activation_pompe",))
        ts._out(("detection_H2O_bas",))
        ts._out(("detection_gaz_haut",))
    else:
        ts._out(("activation_ventilateur",))
        ts._out(("detection_gaz_bas",))


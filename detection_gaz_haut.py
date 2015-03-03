
import linda

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


seuil_CH4 = ts._rd(("seuil_CH4",float))[1]
seuil_C0 = ts._rd(("seuil_C0",float))[1]

def detection_gaz_haut():
    ts._rd(("detection_gaz_haut",))
    niveau_CH4 = ts._rd(("niveau_CH4",float))[1]
    niveau_CO = ts._rd(("niveau_CO",float))[1]
    if niveau_CH4 >= seuil_CH4 and niveau_CO >= seuil_C0:
        ts._out(("activation_ventilateur",))
        print "gaz haut detecte, activation des ventilateurs"
        ts._in(("detection_gaz_haut",))



detection_gaz_haut()
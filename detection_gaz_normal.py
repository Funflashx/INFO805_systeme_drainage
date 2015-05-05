
import linda
import time

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]


seuil_CH4 = ts._rd(("seuil_CH4",float))[1]
seuil_CO = ts._rd(("seuil_CO",float))[1]


def detection_gaz_normal():
    ts._rd(("detection_gaz_normal",))
    niveau_CH4 = ts._rd(("niveau_CH4",float))[1]
    niveau_CO = ts._rd(("niveau_CO",float))[1]
    if niveau_CH4 < (seuil_CH4 - 5) and niveau_CO < (seuil_CO - 5):
        ts._in(("detection_gaz_normal",))
        ts._out(("gaz_normal_detecte",))
    time.sleep(1)
    detection_gaz_normal()

detection_gaz_normal()

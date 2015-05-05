
import linda
import time

linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

seuil_H2O_bas = ts._rd(("seuil_H2O_bas",float))[1]

def detection_H2O_bas():
    ts._rd(("detection_H2O_bas",))
    niveau_H2O = ts._rd(("niveau_H2O",float))[1]
    if (niveau_H2O < seuil_H2O_bas):
        ts._in(("detection_H2O_bas",))
        ts._out(("H2O_bas_detection",))


    time.sleep(1)
    detection_H2O_bas()

detection_H2O_bas()


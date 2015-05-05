import linda
import time

print("surveillance du niveau de l'eau lancee")
linda.connect()
ts = linda.universe._rd(("espace de tuple drainage", linda.TupleSpace))[1]

seuil_CH4 = ts._rd(("seuil_CH4",float))[1]
seuil_CO = ts._rd(("seuil_CO",float))[1]

def surveillance_H2O_haut():

    ts._in(("H2O_haut_detection",))
    niveau_CH4 = ts._rd(("niveau_CH4",float))[1]
    niveau_CO = ts._rd(("niveau_CO",float))[1]
    if niveau_CH4 < seuil_CH4 and niveau_CO < seuil_CO:
        print("activation de la pompe, detection_H2O_bas, detection_gaz_haut")
        ts._out(("pompe_active",))
        ts._out(("detection_H2O_bas",))
        ts._out(("detection_gaz_haut",))

    else:
        print("activation de la pompe impossible car il y a trop de gaz")
        time.sleep(2)
        ts._out(("H2O_haut_detection",))
        # ts._out(("ventilateur_active",))
        # ts._out(("detection_gaz_normal",))
        # etat_ventilateur = ts._rd(("etat_ventilateur",str))[1]
        # if etat_ventilateur == "desactive":
        #     ts._in(("ventilateur_active",))
    time.sleep(2)
    surveillance_H2O_haut()

surveillance_H2O_haut()

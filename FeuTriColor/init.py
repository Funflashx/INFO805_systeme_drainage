import linda

linda.connect()
ts = linda.TupleSpace()
linda.universe._out(("espace de tuple feux", ts))

# initialisation des variables

ts._out(("nb_v_left",2))
ts._out(("nb_v_p",1))
ts._out(("etat_fs_left","Rouge"))
ts._out(("detection_v_haut",))
ts._out(("detection_vs_bas",))

# ts._out(("niveau_CO",5.0))
# ts._out(("etat_pompe","desactive"))
# ts._out(("etat_ventilateur","desactive"))
# ts._out(("detection_H20_haut",))
# ts._out(("detection_gaz_haut",))
#
#
ts._out(("seuil_nb_v",10))
ts._out(("seuil_nb_v_p",15))
ts._out(("etat_fp","Vert"))
print "FEUX PRINCIPAL>  VERT"
ts._out(("etat_fs_right","Rouge"))
print "FEUX SECONDAIRE>  ROUGE"
# ts._out(("seuil_CO",7.0))
# ts._out(("seuil_H2O_haut",100.0))
# ts._out(("seuil_H2O_bas",15.0))
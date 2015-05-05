#!/bin/bash

echo "run main"
python main.py&

echo "run capteurs"
python capteur_CH4.py&
python capteur_CO.py&
python capteur_H2O.py&

echo "run détecteurs"
python detection_gaz_bas.py&
python detection_gaz_haut.py&
python detection_H2O_bas.py&
python detection_H2O_haut.py&


echo "run surveillants"
python surveillance_gaz_haut.py&
python surveillance_H2O_bas.py&
python surveillance_H2O_haut.py&

echo "run Pompe"
python pompe.py&

echo "run Ventilateur"
python ventilateur.py&


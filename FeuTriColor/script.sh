#!/bin/bash

echo "run init"
python init.py&

echo "run capteurs"
python capteur_fs_left.py&
python detecteur_v.py&
python detecteur_v_bas.py&
python feux_principaux.py&
python feux_secondaire.py&
python capteur_fp.py&




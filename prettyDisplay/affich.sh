#!/bin/bash

echo "run affichage"
python writeCH4lvl.py&
python writeCOlvl.py&
python writeH2Olvl.py&
python affichageCH4.py&
python affichageCO.py&
python affichageH2O.py&


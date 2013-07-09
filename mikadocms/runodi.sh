#!/bin/bash
source ~/.bash_profile

workon vcms 
python orig2htm.py data/odietamo.org.uk/odi.ini
python cmsapp.py --config=data/odietamo.org.uk/odi.ini



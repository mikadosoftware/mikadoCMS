#!/bin/bash
source ~/.bash_profile

workon vcms 
python orig2htm.py data/oss4gov.org/oss.ini
python orig2htm.py data/mikadosoftware.com/mikado.ini

#python cmsapp.py --config=data/mikadosoftware.com/mikado.ini
python cmsapp.py --config=data/oss4gov.org/oss.ini


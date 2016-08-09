#!/bin/bash
source ~/.bash_profile

workon vcms
python cmsapp.py --config=data/mikadosoftware.com/mikado_live.ini


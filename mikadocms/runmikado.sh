#!/bin/bash
source ~/.bash_profile

workon vmikado
python cmsapp.py --config=data/mikadosoftware.com/mikado_live.ini


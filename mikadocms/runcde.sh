#!/bin/bash
source ~/.bash_profile

workon vcms 
python cmsapp.py --config=data/cde.com/cde_live.ini


list=`ls *.chp`

for f in $list
do


newf=${f%.chp}.rst

mv $f $newf

done

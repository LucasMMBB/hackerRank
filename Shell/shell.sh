#!/bin/bash

#----Looping with Numbers----

for var in {1..50..1}
do
	echo $var
done

#----The World of Numbers----
read var1
read var2
let sum=$var1+$var2
let diff=$var1-$var2
let prod=$var1*$var2
let quot=$var1/$var2
echo $sum
echo $diff
echo $prod
echo $quot

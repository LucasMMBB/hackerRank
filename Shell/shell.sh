#!/bin/bash

#----Looping with Numbers----

for var in {1..50..1}
do
	echo $var
done

#----The World of Numbers----
<<<<<<< Updated upstream
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


#----Comparing Numbers----
read var1
read var2

if [ $var1 -lt $var2 ]
then
	echo "X is less than Y"
elif [ $var1 -gt $var2 ]
then
	echo "X is greater than Y"
else
	echo "X is equal to Y"
fi

#----Getting started with conditionals----

read var

if [ "$var" == "Y" ] || [ "$var" == "y" ]
then
	echo YES
else
	echo NO
fi
=======
read var1 var2

let "sum = $var1 + $var2"
echo $sum
>>>>>>> Stashed changes

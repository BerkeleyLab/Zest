#!/bin/bash

# bash sub.sh filename config_file
# use for substitution from config file

if [ $# != 2 ]
then
	echo "Usage:
    sub.sh filename config_filenmae"
	exit
fi

sub(){
	old_name=$1
	new_name=$2
	filename=$3
	sed -i "s/$old_name/$new_name/g" $filename
}

cp $1 $1.out

while read line
do
	line=$line" "$1.out
	sub $line
done<$2




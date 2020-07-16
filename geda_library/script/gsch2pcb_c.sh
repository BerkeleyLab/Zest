#!/bin/bash
while [ $# -ne 0 ]
do
	echo '============================================================'
	echo 'Processing file:'
	echo $1
	echo '------------------------------------------------------------'
	gsch2pcb -s $1
	shift
done



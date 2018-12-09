#!/bin/zsh

TESTS_SCRIPT=TestScripts/vgg16.py

EXAMPLE_RESULTS_PATH_PERFORMANCE=Results/CPU/VGG/
IMAGE=Image
SLASH=/
FORMAT=.txt

echo "> Starting Test with $TESTS_SCRIPT"

i=0
while [ "$i" -le 99 ]
do
	j=0
	mkdir -p $EXAMPLE_RESULTS_PATH_PERFORMANCE$IMAGE$i$SLASH
	while [ "$j" -le 99 ]
	do
		touch $EXAMPLE_RESULTS_PATH_PERFORMANCE$IMAGE$i$SLASH$j$FORMAT
		perf stat -a -e cpu-clock,"power/energy-cores/","cpu-cycles/" -o $EXAMPLE_RESULTS_PATH_PERFORMANCE$IMAGE$i$SLASH$j$FORMAT python3 $TESTS_SCRIPT $i
		j=$(( j + 1 ))
	done
	i=$(( i + 1 ))
done

echo "> Finished Test with $TESTS_SCRIPT"

echo "END OF THE TESTS"
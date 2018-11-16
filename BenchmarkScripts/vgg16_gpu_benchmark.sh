#!/bin/zsh

TESTS_SCRIPT=TestScripts/vgg16.py

GPU_RESULTS_PATH=Results/GPU/vgg16Result.csv

echo "> Starting Test with $TESTS_SCRIPT"

touch $GPU_RESULTS_PATH

nvidia-smi --query-gpu=timestamp,power.draw,utilization.gpu,utilization.memory --format=csv -l 1 > $GPU_RESULTS_PATH &

python3 $TESTS_SCRIPT

kill nvidia-smi

echo "> Finished Test with $TESTS_SCRIPT"

echo "END OF THE TESTS"
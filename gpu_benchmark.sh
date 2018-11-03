#!/bin/zsh

echo "> Creating Enviroment"

mkdir -p "Results/GPU/"

sh BenchmarkScripts/resnet50_gpu_benchmark.sh
#!/bin/zsh

echo "> Creating Enviroment"

mkdir -p "Results/CPU/VGG"
mkdir -p "Results/CPU/RESNET50"

echo "==========  Starting Tests =========="
echo "========== Benchmark - CPU =========="

sh BenchmarkScripts/resnet50_cpu_benchmark.sh
sh BenchmarkScripts/vgg16_cpu_benchmark.sh

python3 GraphMaker.py CPU
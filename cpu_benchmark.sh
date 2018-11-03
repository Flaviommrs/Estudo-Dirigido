#!/bin/zsh

echo "> Creating Enviroment"

mkdir -p "Results/Energy/CPU/"
mkdir -p "Results/Performance/CPU/"
mkdir -p "Results/EnergyPerSecond/CPU/"

echo "==========  Starting Tests =========="
echo "========== Benchmark - CPU =========="

sh BenchmarkScripts/resnet50_cpu_benchmark.sh
sh BenchmarkScripts/vgg16_cpu_benchmark.sh
sh BenchmarkScripts/inceptionV3_cpu_benchmark.sh

python3 GraphMaker.py CPU
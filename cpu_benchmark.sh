#!/bin/zsh

echo "> Creating Enviroment"

mkdir -p "Results/Energy/CPU/"
mkdir -p "Results/Performance/CPU/"
mkdir -p "Results/EnergyPerSecond/CPU/"

sh BenchmarkScripts/example_cpu_benchmark.sh

python3 GraphMaker.py CPU
#!/bin/zsh

echo "> Creating Enviroment"

mkdir -p "Results/GPU/"

sh BenchmarkScripts/resnet50_gpu_benchmark.sh
sh BenchmarkScripts/inceptionV3_gpu_benchmark.sh
sh BenchmarkScripts/vgg16_gpu_benchmark.sh
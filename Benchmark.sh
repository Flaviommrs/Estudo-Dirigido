#!/bin/zsh

TESTS_SCRIPT=BenchmarkScripts/example.py

EXAMPLE_RESULTS_PATH_ENERGY=Results/Energy/CPU/ExampleResultsEnergy.txt
EXAMPLE_RESULTS_PATH_PERFORMANCE=Results/Performance/CPU/ExampleResultsPerformance.txt
EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND=Results/EnergyPerSecond/ExampleResultsEnergyPerSecond.txt

echo "==========Começando Testes=========="
echo "==========Benchmark - CPU =========="

echo "> Starting Test with $TESTS_SCRIPT"

touch $EXAMPLE_RESULTS_PATH_ENERGY
touch $EXAMPLE_RESULTS_PATH_PERFORMANCE
touch $EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND

perf stat -a -e "power/energy-cores/" -I 1000 -o $EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND python3 $TESTS_SCRIPT
perf stat -a -e "power/energy-cores/" -o $EXAMPLE_RESULTS_PATH_ENERGY python3 $TESTS_SCRIPT
perf stat -a -o $EXAMPLE_RESULTS_PATH_PERFORMANCE python3 $TESTS_SCRIPT

echo "> Finished Test with $TESTS_SCRIPT"

python3 GraphMaker.py

echo "END OF THE TESTS"
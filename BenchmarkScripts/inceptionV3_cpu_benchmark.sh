TESTS_SCRIPT=TestScripts/inceptionV3.py

EXAMPLE_RESULTS_PATH_ENERGY=Results/Energy/CPU/inceptionV3ResultsEnergy.txt
EXAMPLE_RESULTS_PATH_PERFORMANCE=Results/Performance/CPU/inceptionV3ResultsPerformance.txt
EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND=Results/EnergyPerSecond/CPU/inceptionV3ResultsEnergyPerSecond.txt

echo "> Starting Test with $TESTS_SCRIPT"

touch $EXAMPLE_RESULTS_PATH_ENERGY
touch $EXAMPLE_RESULTS_PATH_PERFORMANCE
touch $EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND

perf stat -a -e "power/energy-cores/" -I 1000 -o $EXAMPLE_RESULTS_PATH_ENERGY_PER_SECOND python3 $TESTS_SCRIPT
perf stat -a -e cpu-clock,"power/energy-cores/","cpu-cycles/" -o $EXAMPLE_RESULTS_PATH_ENERGY python3 $TESTS_SCRIPT

echo "> Finished Test with $TESTS_SCRIPT"

echo "END OF THE TESTS"
cpu : cpu_benchmark.sh
	sh cpu_benchmark.sh

gpu : gpu_benchmark.sh
	sh gpu_benchmark.sh

clean_cpu:
	pip3 uninstall tensorflow
cpu : cpu_benchmark.sh
	sh cpu_benchmark.sh

gpu : gpu_benchmark.sh
	sh gpu_benchmark.sh

clean_cpu:
	pip3 uninstall tensorflow

clean_gpu:
	pip3 uninstall tensorflow-gpu

configure_cpu: clean_gpu
	pip3 install tensorflow

configure_gpu: clean_cpu
	pip3 install tensorflow-gpu

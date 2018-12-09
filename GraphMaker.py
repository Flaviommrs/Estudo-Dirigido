import glob
import matplotlib.pyplot as plt
import os
import sys
import numpy as np

if __name__ == "__main__":

	path = sys.argv[1]

	files = None

	if path == "CPU":
		print ("Making CPU Graphs - This May Take a While")
		vgg_images = glob.glob('Results/CPU/VGG/*')
		resnet_images = glob.glob('Results/CPU/RESNET50/*')
	elif path == "GPU":
		print ("Making GPU Graphs - This May Take a While")
		files = glob.glob('Results/EnergyPerSecond/GPU/*.txt')	

	vgg_energy = []
	vgg_time = []

	for imageDir in vgg_images:

		files = glob.glob('{0}/*.txt'.format(imageDir))

		energy_sum = 0
		time_sum = 0

		number_of_files = 0

		for fileName in files:
			number_of_files = number_of_files + 1
			file = open(fileName, "r+")
			content = [x.strip('\n') for x in file]

			energy_line = content[6]
			
			energy_line = energy_line.split(" ")
			energy_line = list(filter(None, energy_line))

			energy_list = list(energy_line[0])
			for n, i in enumerate(energy_list):
				if i == ',':
					energy_list[n] = '.'

			energy_list = ''.join(energy_list)
			energy = float(energy_list)

			energy_sum = energy + energy_sum

			time_line = content[9]
			time_line = time_line.split(" ")
			time_line = list(filter(None, time_line))

			time_list = list(time_line[0])
			for n, i in enumerate(time_list):
				if i == ',':
					time_list[n] = '.'

			time_list = ''.join(time_list)
			time = float(time_list)

			time_sum = time + time_sum
			file.close()

		vgg_energy.append(energy_sum/number_of_files)
		vgg_time.append(time_sum/number_of_files)

	resnet_energy = []
	resnet_time = []

	for imageDir in resnet_images:
		files = glob.glob('{0}/*.txt'.format(imageDir))

		energy_sum = 0
		time_sum = 0

		number_of_files = 0

		for fileName in files:
			number_of_files = number_of_files + 1
			file = open(fileName, "r+")
			content = [x.strip('\n') for x in file]

			energy_line = content[6]
			
			energy_line = energy_line.split(" ")
			energy_line = list(filter(None, energy_line))

			energy_list = list(energy_line[0])
			for n, i in enumerate(energy_list):
				if i == ',':
					energy_list[n] = '.'

			energy_list = ''.join(energy_list)
			energy = float(energy_list)

			energy_sum = energy + energy_sum

			time_line = content[9]
			time_line = time_line.split(" ")
			time_line = list(filter(None, time_line))

			time_list = list(time_line[0])
			for n, i in enumerate(time_list):
				if i == ',':
					time_list[n] = '.'

			time_list = ''.join(time_list)
			time = float(time_list)

			time_sum = time + time_sum
			file.close()

		resnet_energy.append(energy_sum/number_of_files)
		resnet_time.append(time_sum/number_of_files)

	label = ["image {}".format(i) for i in range(1, 101)]

	figsize = 1920/80, 1080/80

	fig, ax = plt.subplots(dpi=80, figsize=figsize)
	ax.bar(label,vgg_energy,width=0.8, align='center', edgecolor='gray')
	plt.ylabel('Energy (joules)')
	plt.xticks(rotation=90)
	plt.savefig('Results/CPU/VGG/ImagesEnergy.png')
	plt.close()

	fig, ax = plt.subplots(dpi=80, figsize=figsize)
	ax.bar(label,vgg_time,width=0.8, align='center', edgecolor='gray')
	plt.ylabel('Time (s)')
	plt.xticks(rotation=90)
	plt.savefig('Results/CPU/VGG/ImagesTime.png')
	plt.close()

	fig, ax = plt.subplots(dpi=80, figsize=figsize)
	ax.bar(label,resnet_energy,width=0.8, align='center', edgecolor='gray')
	plt.ylabel('Energy (joules)')
	plt.xticks(rotation=90)
	plt.savefig('Results/CPU/RESNET50/ImagesEnergy.png')
	plt.close()

	fig, ax = plt.subplots(dpi=80, figsize=figsize)
	ax.bar(label,resnet_time,width=0.8, align='center', edgecolor='gray')
	plt.ylabel('Time (s)')
	plt.xticks(rotation=90)
	plt.savefig('Results/CPU/RESNET50/ImagesTime.png')
	plt.close()

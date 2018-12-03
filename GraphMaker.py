import glob
import matplotlib.pyplot as plt
import os
import sys

if __name__ == "__main__":

	path = sys.argv[1]

	files = None

	if path == "CPU":
		print ("Making CPU Graphs - This May Take a While")
		vgg_images = glob.glob('Results/CPU/VGG/*')
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

			print("energy: {}".format(energy))

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

			print("time: {}".format(time))

		vgg_energy.append(energy_sum/number_of_files)
		vgg_time.append(time_sum/number_of_files)































			# time_stamp = []
			# energy = []

			# for line in content:
			# 	if not line or line[0] == '#':
			# 		continue

			# 	line_content = line.split(" ")
			# 	line_content = list(filter(None, line_content))

			# 	energy_list = list(line_content[1])
			# 	for n, i in enumerate(energy_list):
			# 		if i == ',':
			# 			energy_list[n] = '.'

			# 	energy_list = ''.join(energy_list)

			# 	time_stamp.append(int(float(line_content[0])))
			# 	energy.append(float(energy_list))

			# path, name = os.path.split(fileName)
			# name, _= os.path.splitext(name)
			# plt.plot(time_stamp, energy)
			# plt.xlabel('Time')
			# plt.ylabel('Energy (power)')
			# plt.savefig(path + '/'+ name + '.png')
			# plt.clf()
			# file.close()
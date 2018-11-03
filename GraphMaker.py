import glob
import matplotlib.pyplot as plt
import os
import sys

if __name__ == "__main__":

	path = sys.argv[1]

	files = None

	if path == "CPU":
		print ("Making CPU Graphs - This May Take a While")
		files = glob.glob('Results/EnergyPerSecond/CPU/*.txt')
	elif path == "GPU":
		print ("Making GPU Graphs - This May Take a While")
		files = glob.glob('Results/EnergyPerSecond/GPU/*.txt')	

	for fileName in files:
		file = open(fileName, "r+")
		content = [x.strip('\n') for x in file]

		time_stamp = []
		energy = []

		for line in content:
			if not line or line[0] == '#':
				continue

			line_content = line.split(" ")
			line_content = list(filter(None, line_content))

			energy_list = list(line_content[1])
			for n, i in enumerate(energy_list):
				if i == ',':
					energy_list[n] = '.'

			energy_list = ''.join(energy_list)

			time_stamp.append(int(float(line_content[0])))
			energy.append(float(energy_list))

		path, name = os.path.split(fileName)
		name, _= os.path.splitext(name)
		plt.plot(time_stamp, energy)
		plt.xlabel('Time')
		plt.ylabel('Energy (power)')
		plt.savefig(path + '/'+ name + '.png')
		plt.clf()
		file.close()
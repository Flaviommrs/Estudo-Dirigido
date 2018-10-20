import glob
import matplotlib.pyplot as plt
import os

print ("Making Graphs - This Make Take a While")

files = glob.glob('Results/EnergyPerSecond/*.txt')

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
	plt.ylabel('Energy (J)')
	plt.savefig('Results/EnergyPerSecond/' + name + '.png')


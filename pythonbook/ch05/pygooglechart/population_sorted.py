#!/usr/bin/env python2

from pygooglechart import PieChart3D
from operator import itemgetter

with open('population.csv') as f:
	population = map(lambda x: [x[0], int(x[1])],\
    	[line.strip().split(",") for line in f])

sorted_population = sorted(population, key=itemgetter(1),\
	reverse=True)

labels = map(lambda x: x[0].decode('cp949').encode('utf-8'),\
	sorted_population)
data = map(lambda x: x[1], sorted_population)

chart = PieChart3D(500, 200)
chart.add_data(data)
chart.set_pie_labels(labels)
print chart.get_url()

chart.download('population_sorted.png')

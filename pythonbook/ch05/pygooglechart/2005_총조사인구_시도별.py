#!python2
#!-*- encoding: cp949 -*-

from pygooglechart import PieChart3D

with open('2005_총조사인구_시도별.csv') as f:
	population = [line.strip().split(",") for line in f]
print population

labels = map(lambda x: x[0].decode('cp949').encode('utf-8'), population)
data = map(lambda x: int(x[1]), population)

chart = PieChart3D(500, 200)
chart.add_data(data)
chart.set_pie_labels(labels)
print chart.get_url()

chart.download('2005_총조사인구_시도별.png')

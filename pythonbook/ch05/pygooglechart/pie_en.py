#!/usr/bin/env python2

from pygooglechart import PieChart3D

chart = PieChart3D(250, 100)
chart.add_data([20, 10])
chart.set_pie_labels(['Hello', 'World'])
chart.download('pie_en.png')

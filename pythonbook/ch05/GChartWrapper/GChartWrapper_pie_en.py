#!/usr/bin/env python

from GChartWrapper import Pie

chart = Pie([20, 10])
chart.title('Hello GChartWrapper')
chart.label('hello', 'world')
chart.save('pie_en.png')
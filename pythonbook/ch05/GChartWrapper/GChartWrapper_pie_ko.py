#!/usr/bin/env python3

from GChartWrapper import Pie

chart = Pie([20, 10])
chart.title('안녕 GChartWrapper')
chart.label('안녕', '세상')
chart.save('pie_ko.png')
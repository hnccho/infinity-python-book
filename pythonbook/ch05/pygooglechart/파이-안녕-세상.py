#!C:\Python27\python.exe
#!-*- encoding: cp949 -*-

from pygooglechart import PieChart3D

chart = PieChart3D(250, 100)
chart.add_data([20, 10])
chart.set_pie_labels([u'안녕'.encode('utf-8'), u'세상'.encode('utf-8')])
print chart.get_url()
chart.download('파이-안녕-세상.png')
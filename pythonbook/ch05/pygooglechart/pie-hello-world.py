#!C:\Python27\python.exe

from pygooglechart import PieChart3D

chart = PieChart3D(250, 100)
chart.add_data([20, 10])
chart.set_pie_labels(['Hello', 'World'])
chart.download('pie-hello-world.png')

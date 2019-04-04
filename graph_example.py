from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg


l = QtGui.QVBoxLayout()


pw3 = pg.PlotWidget()
l.addWidget(pw3)

lr = pg.LinearRegionItem([1, 30], bounds=[0,100], movable=True)
pw3.addItem(lr)
import sys
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtGui, QtCore
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa')
        self.setCentralWidget(self.graphWidget)

        # hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        # temperature_2 = [50, 35, 44, 22, 38, 32, 27, 38, 32, 44]
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0, 100) for _ in range(100)]  # 100 data points

        # self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa')
        # self.graphWidget.setBackground((100,50,255)) # RGB each 0-255
        # self.graphWidget.setBackground((100,50,255,25))
        # self.graphWidget.setBackground(QtGui.QColor(100,50,254,25))
        color = self.palette().color(QtGui.QPalette.Window)  # Get the default window background,
        self.graphWidget.setBackground(color)
        pen = pg.mkPen(color=(255, 0, 0), width=5)

        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")

        styles = {'color': 'red', 'font-size': '30pt'}
        self.graphWidget.setLabel('left', 'Temp. (C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

        self.graphWidget.addLegend()

        self.graphWidget.showGrid(x=True, y=True)

        #self.graphWidget.setXRange(0, 10, padding=0)
        #self.graphWidget.setYRange(20, 55, padding=0)

        # self.plot(hour, temperature, 'Sensor 1', 'r')
        # self.plot(hour, temperature_2, 'Sensor 2', 'g')
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    # def plot(self, x, y, plotname, color):
    #     pen = pg.mkPen(color=color)
    #     self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))

    def update_plot_data(self):
        self.x = self.x[1:] # Remove the first y element.
        self.x.append(self.x[-1] + 1) # Add a new value 1 higher than the last.
        self.y = self.y[1:] # Remove the first
        self.y.append(randint(0, 100)) # Add a new random value.
        self.data_line.setData(self.x, self.y)  # Update the data.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec()
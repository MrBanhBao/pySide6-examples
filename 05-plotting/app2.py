import sys
import random
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QMainWindow, QApplication# import PySide6 before matplotlib
import matplotlib
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

matplotlib.use("QtAgg")


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]

        # We need to store a reference to the plotted line
        # somewhere, so we can apply the new data to it.
        self._plot_ref = None
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        #self.xdata = self.xdata[1:] # Remove the first y element.
        #self.xdata.append(self.xdata[-1] + 1) # Add a new value 1 higher than the last.

        # Note: we no longer need to clear the axis.
        if self._plot_ref is None:
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, "r")
            self._plot_ref = plot_refs[0]
        else:
            self._plot_ref.set_xdata(self.xdata)
            self._plot_ref.set_ydata(self.ydata)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
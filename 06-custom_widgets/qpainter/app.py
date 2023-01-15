import sys
from random import randint, choice

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(2)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)

        for n in range(10000):
            colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200+randint(-100, 100),  # x
                150+randint(-100, 100)   # y
            )

        pen.setColor(QtGui.QColor('blue'))
        pen.setWidth(15)
        painter.setPen(pen)
        painter.drawLine(
            QtCore.QPoint(100, 100),
            QtCore.QPoint(300, 200)
        )

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.Dense1Pattern)
        painter.setBrush(brush)

        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#EB5160"))
        painter.setPen(pen)
        painter.drawRect(50, 50, 100, 100)
        painter.drawRect(60, 60, 150, 100)
        painter.drawRect(70, 70, 100, 150)
        painter.drawRect(80, 80, 150, 100)
        painter.drawRect(90, 90, 100, 150)

        pen.setWidth(3)
        painter.setBrush(Qt.NoBrush)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)
        painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
        painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
        painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
        painter.drawRoundedRect(160, 160, 100, 100, 50, 50)

        pen.setWidth(3)
        pen.setColor(QtGui.QColor(204,0,0))  # r, g, b
        painter.setPen(pen)

        painter.drawEllipse(10, 10, 100, 100)
        painter.drawEllipse(10, 10, 150, 200)
        painter.drawEllipse(10, 10, 200, 300)


        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(100, 100, 'Hello, world!')
        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
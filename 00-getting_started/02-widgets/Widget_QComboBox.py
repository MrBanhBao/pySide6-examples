import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()

        # insert custom test
        widget.setEditable(True)
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        # limit items
        widget.setMaxCount(10)
        widget.addItems(["One", "Two", "Three"])

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
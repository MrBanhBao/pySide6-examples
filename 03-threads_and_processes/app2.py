from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QRunnable, Slot, QThreadPool

import sys
import time


class Worker(QRunnable):
    '''
    Worker thread
    '''

    @Slot()  # QtCore.Slot
    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        time.sleep(5)
        print("Thread complete")


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        c = QPushButton("?")
        c.pressed.connect(self.change_message)

        layout.addWidget(self.l)
        layout.addWidget(b)

        layout.addWidget(c)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

    def change_message(self):
        self.message = "OH NO"
        print(self.message)

    def oh_no(self):
        self.message = "Pressed"

        worker = Worker()
        self.threadpool.start(worker)
        print(self.message)



app = QApplication(sys.argv)
window = MainWindow()
app.exec_()
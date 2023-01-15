import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.button_is_checked = True

        self.setWindowTitle('My App')

        # !!! Clocked directly transmit value
        # button = QPushButton("Press Me!")
        # button.setCheckable(True)
        # button.clicked.connect(self.the_button_was_clicked) # signal.connect(slot) slot->function
        # button.clicked.connect(self.the_button_was_toggled)
        # button.setChecked(self.button_is_checked)

        # self.setCentralWidget(button)

        # !!! Released don't so we need to get value manually
        self.button = QPushButton('Release me.')
        self.button.setCheckable(True)
        self.button.setChecked(self.button_is_checked)

        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.released.connect(self.the_button_was_released)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        # changed text properties
        self.button.setText('You already clicked me.')
        self.button.setEnabled(False)

        # changed Window Titles
        self.setWindowTitle('DEADLOCK!!!')

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print('checked: ', checked)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked()
        print('Released! checked: ', self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
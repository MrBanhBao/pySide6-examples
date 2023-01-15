# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


def load_ui(path):
    loader = QUiLoader()
    path = os.fspath(path)
    ui_file = QFile(path)
    ui_file.open(QFile.ReadOnly)
    ui = loader.load(ui_file)
    ui_file.close()
    return ui


if __name__ == "__main__":
    app = QApplication([])
    widget = load_ui('form.ui')
    widget.show()
    sys.exit(app.exec())

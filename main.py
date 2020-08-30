import sys
from PySide2 import QtWidgets, QtGui, QtCore
from gui.main_window import MainWindow
from gui.appearence.appearence import *

class Main(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.setStyle(QtWidgets.QStyleFactory.create("fusion"))
        set_theme_by_current_time(self)
    def start(self):
        window = MainWindow(self)
        window.show()

if __name__ == "__main__":
    main = Main()
    main.start()
    sys.exit(main.exec_())


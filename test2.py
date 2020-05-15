import re
import operator
import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

        self.tabledata = [('apple', 'red', 'small'),
                          ('apple', 'red', 'medium'),
                          ('apple', 'green', 'small'),
                          ('banana', 'yellow', 'large')]
        self.header = ['fruit', 'color', 'size']

        # create table
        self.createTable()

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.tv)
        self.setLayout(layout)

    def popup(self, pos):
        for i in self.tv.selectionModel().selection().indexes():
            print (i.row(), i.column())
        menu = QMenu()
        quitAction = menu.addAction("Quit")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == quitAction:
            qApp.quit()

    def createTable(self):
        # create the view
        self.tv = QTableView()
        self.tv.setStyleSheet("gridline-color: rgb(191, 191, 191)")

        self.tv.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tv.customContextMenuRequested.connect(self.popup)

        # set the table model
        tm = MyTableModel(self.tabledata, self.header, self)
        self.tv.setModel(tm)

        # set the minimum size
        self.tv.setMinimumSize(400, 300)

        # hide grid
        self.tv.setShowGrid(True)

        # set the font
        font = QFont("Calibri (Body)", 12)
        self.tv.setFont(font)

        # hide vertical header
        vh = self.tv.verticalHeader()
        vh.setVisible(False)

        # set horizontal header properties
        hh = self.tv.horizontalHeader()
        hh.setStretchLastSection(True)

        # set column width to fit contents
        self.tv.resizeColumnsToContents()

        # set row height
        nrows = len(self.tabledata)
        for row in xrange(nrows):
            self.tv.setRowHeight(row, 18)

        # enable sorting
        self.tv.setSortingEnabled(True)

        return self.tv

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """ datain: a list of lists
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))

if __name__ == "__main__":
    main()
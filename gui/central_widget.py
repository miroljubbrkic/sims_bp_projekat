from PySide2 import QtWidgets, QtGui, QtCore
from gui.model import Model

from gui.form import Form

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent, data_list):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.data_list = data_list
        self.tab_widget = None

        self.model = Model(self.data_list)
        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
 
        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.handleHeaderMenu)


        
        self.main_layout.addWidget(self.table)
        self.setLayout(self.main_layout)

    def data_object_selected(self, index):
        model = self.table.model(self.data_list)
        selected_object_model = model.get_element(index)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)



    def remove_one(self):
        indexes = self.table.selectionModel().selectedIndexes()
        for index in indexes:
            self.table.model().removeRows(index.row(), 1, index)
            break

    def handle_header_menu(self):
        menu = QtWidgets.QMenu(self)
        delete = QtWidgets.QAction("Delete", menu)

        delete.triggered.connect(lambda : self.remove_one())
        menu.addAction(delete)
        add = QtWidgets.QAction("Add", menu)
        add.triggered.connect(lambda : self.table.model().insertRows(1, 1, QtCore.QModelIndex()))
        menu.addAction(add)
        menu.exec_(QtGui.QCursor.pos())
    


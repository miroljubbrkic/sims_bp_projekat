from PySide2 import QtWidgets, QtGui, QtCore
from gui.model import Model

from gui.form import Form

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent, data_list):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.data_list = data_list
        self.subtables = []
        self.tab_widget = None
        # self.create_tab_widget()

        for i in range(len(self.data_list.metadata["linked_files"])):
            self.subtables.append(QtWidgets.QTableView(self.tab_widget))


        self.model = Model(self.data_list)
        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setModel(self.model)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        # subtable test
        self.table.clicked.connect(self.show_tabs)


    
        self.tool_bar = QtWidgets.QToolBar()
        self.tool_bar.setMovable(False)
        self.tool_bar.setFloatable(False)
        tool_bar_add = QtWidgets.QAction("ADD", self.tool_bar)
        tool_bar_add.triggered.connect(lambda : self.table.model().insertRows(1, 1, QtCore.QModelIndex()))
        self.tool_bar.addAction(tool_bar_add)
        tool_bar_delete = QtWidgets.QAction("DELETE", self.tool_bar)
        tool_bar_delete.triggered.connect(lambda : self.remove_one())
        self.tool_bar.addAction(tool_bar_delete)

        self.table.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.handle_header_menu)


        self.main_layout.addWidget(self.tool_bar)
        self.main_layout.addWidget(self.table)
        if len(self.subtables) > 0:
            self.create_tab_widget()
            self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def data_object_selected(self, index):
        model = self.table.model(self.data_list)
        selected_object_model = model.get_element(index)
       
        
    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def show_tabs(self):
        for i in self.subtables:
            self.tab_widget.addTab(i, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")

    def remove_one(self):
        indexes = self.table.selectionModel().selectedIndexes()
        for index in indexes:
            self.table.model().removeRows(index.row(), 1, index)
            break
        
    def handle_header_menu(self):
        menu = QtWidgets.QMenu(self)
        add = QtWidgets.QAction("Add", menu)
        add.triggered.connect(lambda : self.table.model().insertRows(1, 1, QtCore.QModelIndex()))
        menu.addAction(add)
        delete = QtWidgets.QAction("Delete", menu)
        delete.triggered.connect(lambda : self.remove_one())
        menu.addAction(delete)
        menu.exec_(QtGui.QCursor.pos())
    
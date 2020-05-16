from PySide2 import QtWidgets, QtGui, QtCore
from gui.model import Model

# from gui.forme.student_forma import StudentForma

class CentralWidget(QtWidgets.QWidget):
    def __init__(self, parent, data_list):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.data_list = data_list
        self.tab_widget = None
        # self.create_tab_widget()

        self.model = Model(self.data_list)
        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setModel(self.model)
        # za tabelu dodato da resize za max podataka
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        # QtWidgets.QHeaderView.stretchLastSection


        # self.subtable = QtWidgets.QTableView(self.tab_widget)
        # self.subtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.subtable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.table.clicked.connect(self.data_object_selected)

        # self.subtable2 = QtWidgets.QTableView(self.tab_widget)

        # self.dodaj_studenta = StudentForma(self.model.students)
        # self.tab_widget.addTab(self.dodaj_studenta,"Dodaj studenta")

        # self.tab_widget.addTab(self.subtable, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")
        # self.tab_widget.addTab(self.subtable2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")
    

        self.main_layout.addWidget(self.table)
        # self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def data_object_selected(self, index):
        model = self.table.model(self.data_list)
        selected_obect_model = model.get_element(index)

        # polozeni_predmeti_model = self.create_polozeni_predmeti_model(student)
        # self.subtable.setModel(polozeni_predmeti_model)

        # self.tab_widget.addTab(self.subtable, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")

        
    # def create_tab_widget(self):
    #     self.tab_widget = QtWidgets.QTabWidget(self)
    #     self.tab_widget.setTabsClosable(True)
    #     self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    # def create_polozeni_predmeti_model(self, student):
    #     polozeni_predmeti_model = PolozeniPredmetModel(self.model.students)
    #     polozeni_predmeti_model.polozeni_predmeti = student.polozeni_predmeti

    #     return polozeni_predmeti_model

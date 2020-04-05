from PySide2 import QtWidgets, QtGui, QtCore
from database.komponente.nastavnik import Nastavnik
from gui.forme.nastavnik_forma import NastavnikForma
from gui.modeli.nastavnik_model import NastavnikModel

class NastavnikWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.nastavnik_model = self.create_nastavnik_dummy_model()
 
        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setModel(self.nastavnik_model)

        self.dodaj_nastavnika = NastavnikForma(self.nastavnik_model.nastavnici)

        self.tab_widget.addTab(self.dodaj_nastavnika,"Dodaj nastavnika")


        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def nastavnik_selected(self, index):
        model = self.table1.model()
        nastavnik = model.get_element(index)
 

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_nastavnik_dummy_model(self):
        nastavnik_model = NastavnikModel()
        
        if len(nastavnik_model.nastavnici.get_all()) == 0:      
            nastavnik_model.nastavnici.insert_many([
                Nastavnik("1","Petar","Markovic", "01.01.1970","Profesor"),
                Nastavnik("2","Tomislav","Tomic", "08.03.1992","Asistent"),
                Nastavnik("3","Klaudija","Petrovic","05.05.1986","Profesor")
            ])
        return nastavnik_model
from PySide2 import QtWidgets, QtGui, QtCore
from database.komponente.predmet import Predmet
from database.komponente.nastavnik import Nastavnik
from gui.modeli.predmet_nastavnik_model import PredmetNastavnikModel
from gui.forme.predmet_forma import PredmetForma
from gui.modeli.predmet_model import PredmetModel

class PredmetWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.predmet_model = self.create_predmet_dummy_model()
 
        # tabele kao atributi a ne kao lokalne promenljive
        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setModel(self.predmet_model)

        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.subtable1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.clicked.connect(self.predmet_selected)

        self.dodaj_predmet = PredmetForma(self.predmet_model.predmeti)

        self.tab_widget.addTab(self.dodaj_predmet,"Dodaj predmet")

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Nastavnici")
        

        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def predmet_selected(self, index):
        model = self.table1.model()
        predmet = model.get_element(index)

        predmet_nastavnik_model = self.create_predmet_nastavnik_model(predmet)
        self.subtable1.setModel(predmet_nastavnik_model)

        self.tab_widget.addTab(self.subtable1, QtGui.QIcon("icons8-edit-file-64.png"), "Nastavnik")
       

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        # self.tab_widget.setTabsClosable(True)
        # self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_predmet_dummy_model(self):
        predmet_model = PredmetModel()
        
        if len(predmet_model.predmeti.get_all()) == 0:      
            predmet_model.predmeti.insert_many([
                Predmet("1","oop1","nema",3,2,[
                    Nastavnik("1","Petar","Markovic", "01.01.1970","Profesor"),
                    Nastavnik("2","Tomislav","Tomic", "08.03.1992","Asistent"),
                    ]),
                Predmet("2","wp","nema",3,3,[
                    Nastavnik("2","Tomislav","Tomic", "08.03.1992","Asistent"),
                    Nastavnik("3","Klaudija","Petrovic", "05.05.1986","Profesor")
                ]),
                Predmet("3","sims","nema",3,4,[
                    Nastavnik("2","Tomislav","Tomic", "08.03.1992","Asistent"),
                    Nastavnik("3","Klaudija","Petrovic", "05.05.1986","Profesor")
                ])
            ])
        return predmet_model

    def create_predmet_nastavnik_model(self, predmet):
        """
        Za odabranog studenta pravi model za tabelu polozenih predmeta
        """
        nastavnik_model = PredmetNastavnikModel(self.predmet_model.predmeti)
        nastavnik_model.nastavnici = predmet.nastavnici

        return nastavnik_model




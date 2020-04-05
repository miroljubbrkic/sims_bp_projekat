from PySide2 import QtWidgets, QtGui, QtCore
from database.komponente.student import Student
from database.komponente.polozeni_predmet import PolozeniPredmet
from database.komponente.nepolozeni_predmet import NepolozeniPredmet
from gui.modeli.student_model import StudentModel
from gui.modeli.polozeni_predmet_model import PolozeniPredmetModel
from gui.modeli.nepolozeni_predmet_model import NepolozeniPredmetModel
from gui.forme.student_forma import StudentForma
from gui.brisanje.student_brisanje import StudentBrisanje




class StudentWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.student_model = self.create_student_dummy_model()


        self.table1 = QtWidgets.QTableView(self.tab_widget)
        self.table1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.setModel(self.student_model)

        self.dodaj_studenta = StudentForma(self.student_model.students)



        self.subtable1 = QtWidgets.QTableView(self.tab_widget)
        self.subtable1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.subtable1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table1.clicked.connect(self.student_selected)

        self.subtable2 = QtWidgets.QTableView(self.tab_widget)
        
        self.brisanje = StudentBrisanje(self.student_model.students,None)

        self.tab_widget.addTab(self.dodaj_studenta,"Dodaj studenta")
        self.tab_widget.addTab(self.subtable1,"Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2,"Nepolozeni predmeti")
        self.tab_widget.addTab(self.brisanje,"Ukloni studenta")
        
    
        self.main_layout.addWidget(self.table1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):
        model = self.table1.model()
        student = model.get_element(index)

        polozeni_predmeti_model = self.create_polozeni_predmeti_model(student)
        self.subtable1.setModel(polozeni_predmeti_model)

        nepolozeni_predmeti_model = self.create_nepolozeni_predmeti_model(student)
        self.subtable2.setModel(nepolozeni_predmeti_model)

        self.brisanje = StudentBrisanje(self.student_model.students,student.broj_indeksa)


        self.tab_widget.addTab(self.subtable1, "Polozeni predmeti")
        self.tab_widget.addTab(self.subtable2, "Nepolozeni predmeti")
        self.tab_widget.addTab(self.brisanje, "Ukloni studenta")
          

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_student_dummy_model(self):
        student_model = StudentModel()

        if len(student_model.students.get_all()) == 0:      
            student_model.students.insert_many([
                Student("2018270000", "Marko Markovic", [
                    PolozeniPredmet("SIMS","1", "2", "3", 10),
                    PolozeniPredmet("BP","11", "22", "22", 8),
                    PolozeniPredmet("TS","33", "33", "33", 9)
                ],
                [
                    NepolozeniPredmet("AR","ne", "ne", "da", 1),
                    NepolozeniPredmet("WD","ef", "efe", "wefw", 2),
                    NepolozeniPredmet("WP","efefe", "fefe", "fefe", 9)
                ]),
                Student("2018270001", "Janko Jankovic", [
                    PolozeniPredmet("OP","", "", "", 10),
                    PolozeniPredmet("OOP1","", "", "", 8),
                    PolozeniPredmet("OOP2","", "", "", 9)
                ],
                [
                    NepolozeniPredmet("SIMS","", "", "", 1),
                    NepolozeniPredmet("WD","", "", "", 2),
                    NepolozeniPredmet("TS","", "", "", 3)
                ]),
                Student("2018270002", "Petar Petrovic", [
                    PolozeniPredmet("AR","", "", "", 10),
                    PolozeniPredmet("WP","", "", "", 8),
                    PolozeniPredmet("WD","", "", "", 9)
                ],
                [
                    NepolozeniPredmet("OP","", "", "", 1),
                    NepolozeniPredmet("OOP1","", "", "", 2),
                    NepolozeniPredmet("OOP2","", "", "", 9)
                ]),
                Student("2018270003", "Sima Simic", [
                    PolozeniPredmet("DM","", "", "", 10),
                    PolozeniPredmet("EJ1","", "", "", 8),
                    PolozeniPredmet("MEN","", "", "", 9)
                ]),
                Student("2018270004", "Lazar Lazarevic")
            ])
        return student_model

    def create_polozeni_predmeti_model(self, student):
        polozeni_predmeti_model = PolozeniPredmetModel(self.student_model.students)
        polozeni_predmeti_model.polozeni_predmeti = student.polozeni_predmeti

        return polozeni_predmeti_model

    def create_nepolozeni_predmeti_model(self, student):
        nepolozeni_predmeti_model = NepolozeniPredmetModel(self.student_model.students)
        nepolozeni_predmeti_model.nepolozeni_predmeti = student.nepolozeni_predmeti

        return nepolozeni_predmeti_model
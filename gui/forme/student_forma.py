from PySide2 import QtWidgets, QtCore
from database.komponente.student import Student
from database.komponente.polozeni_predmet import PolozeniPredmet
from database.komponente.nepolozeni_predmet import NepolozeniPredmet

class StudentForma(QtWidgets.QDialog):
    def __init__(self, studenti):
        super().__init__()
        self.studenti = studenti
        formLayout = QtWidgets.QFormLayout()

        self.broj_indeksa = QtWidgets.QLineEdit()
        self.ime_prezime = QtWidgets.QLineEdit()
       
        formLayout.addRow(QtWidgets.QLabel("Sifra predmeta: "), self.broj_indeksa)
        formLayout.addRow(QtWidgets.QLabel("ime_prezime: "), self.ime_prezime)
    
        btnOk = QtWidgets.QPushButton("Dodaj")
        btnOk.clicked.connect(self.dodaj_studenta)
        
        group = QtWidgets.QDialogButtonBox()
        group.addButton(btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        
        formLayout.addRow(group)

        self.setLayout(formLayout)
        
    def dodaj_studenta(self):
        if self.broj_indeksa.text() == "" or self.ime_prezime.text() == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Sva polja moraju biti popunjena!")
            msgBox.exec()
        else:
            p1 = PolozeniPredmet("1234","","","",[],"")
            p2 = PolozeniPredmet("222","","","",[],"")
            
            n1 = NepolozeniPredmet("155","","","",[],"")
            n2 = NepolozeniPredmet("77","","","",[],"")

            novi_student = Student(self.broj_indeksa.text(),self.ime_prezime.text(),[p1,p2],[n1,n2]) 
            self.studenti.insert(novi_student)
            self.studenti.load_data()

            self.broj_indeksa.setText("")
            self.ime_prezime.setText("")
        return
        
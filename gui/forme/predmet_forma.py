from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler
import pickle
from database.komponente.predmet import Predmet

class PredmetForma(QtWidgets.QDialog):
    def __init__(self,predmeti):
        

        super().__init__()
        formLayout = QtWidgets.QFormLayout()
        self.predmeti = predmeti
    
        self.sifra_predmeta = QtWidgets.QLineEdit()
        self.naziv = QtWidgets.QLineEdit()
        self.silabus = QtWidgets.QLineEdit()
        self.broj_casova_nedeljno = QtWidgets.QLineEdit()
        self.broj_semestra = QtWidgets.QLineEdit()
        
        formLayout.addRow(QtWidgets.QLabel("Sifra predmeta: "), self.sifra_predmeta)
        formLayout.addRow(QtWidgets.QLabel("Naziv: "), self.naziv)
        formLayout.addRow(QtWidgets.QLabel("Silabus: "), self.silabus)
        formLayout.addRow(QtWidgets.QLabel("Broj casova nedeljno: "), self.broj_casova_nedeljno)
        formLayout.addRow(QtWidgets.QLabel("Broj semestra: "), self.broj_semestra)


        btnOk = QtWidgets.QPushButton("Dodaj")
        btnOk.clicked.connect(self.dodaj_predmet)
        
        group = QtWidgets.QDialogButtonBox()
        group.addButton(btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        
        formLayout.addRow(group)
        
        
        
        self.setLayout(formLayout)
        
    def dodaj_predmet(self):
        if self.sifra_predmeta.text() == "" or self.naziv.text() == "" or self.silabus.text() == "" or self.broj_casova_nedeljno.text() == "" or self.broj_semestra.text() == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Sva polja moraju biti popunjena")
            msgBox.exec()
        else:
            novi_predmet = Predmet(self.sifra_predmeta.text(),self.naziv.text(),self.silabus.text(),self.broj_casova_nedeljno.text(),self.broj_semestra.text(),[]) 
            self.predmeti.insert(novi_predmet)
            self.predmeti.load_data()
            
           
            self.sifra_predmeta.setText("")
            self.naziv.setText("")
            self.silabus.setText("")
            self.broj_casova_nedeljno.setText("")
            self.broj_semestra.setText("")

            return self.predmeti.get_all()

from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler
import pickle
from database.komponente.nastavnik import Nastavnik

class NastavnikForma(QtWidgets.QDialog):
    def __init__(self,nastavnici):
        

        super().__init__()
        formLayout = QtWidgets.QFormLayout()
        self.nastavnici = nastavnici
    
        self.sifra_zaposlenog = QtWidgets.QLineEdit()
        self.ime = QtWidgets.QLineEdit()
        self.prezime = QtWidgets.QLineEdit()
        self.datum_rodjenja = QtWidgets.QLineEdit()
        self.tip = QtWidgets.QLineEdit()
        
        formLayout.addRow(QtWidgets.QLabel("Sifra zaposlenog: "), self.sifra_zaposlenog)
        formLayout.addRow(QtWidgets.QLabel("Ime: "), self.ime)
        formLayout.addRow(QtWidgets.QLabel("Prezime: "), self.prezime)
        formLayout.addRow(QtWidgets.QLabel("Datum rodjenja: "), self.datum_rodjenja)
        formLayout.addRow(QtWidgets.QLabel("Tip: "), self.tip)


        btnOk = QtWidgets.QPushButton("Dodaj")
        btnOk.clicked.connect(self.dodaj_nastavnika)
        
        group = QtWidgets.QDialogButtonBox()
        group.addButton(btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        
        formLayout.addRow(group)
        
        
        
        self.setLayout(formLayout)
        
    def dodaj_nastavnika(self):
        if self.sifra_zaposlenog.text() == "" or self.ime.text() == "" or self.prezime.text() == "" or self.datum_rodjenja.text() == "" or self.tip.text() == "":
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Sva polja moraju biti popunjena")
            msgBox.exec()
        else:
            novi_nastavnik = Nastavnik(self.sifra_zaposlenog.text(),self.ime.text(),self.prezime.text(),self.datum_rodjenja.text(),self.tip.text()) 
            self.nastavnici.insert(novi_nastavnik)
            self.nastavnici.load_data()
            
           
            self.sifra_zaposlenog.setText("")
            self.ime.setText("")
            self.prezime.setText("")
            self.datum_rodjenja.setText("")
            self.tip.setText("")

            return self.nastavnici.get_all()

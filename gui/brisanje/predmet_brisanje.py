from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler
import pickle
from database.komponente.student import Student
from database.komponente.polozeni_predmet import PolozeniPredmet
from database.komponente.nepolozeni_predmet import NepolozeniPredmet

class StudentBrisanje(QtWidgets.QDialog):
    def __init__(self,studenti,id):
        super().__init__()
        formLayout = QtWidgets.QFormLayout()
        self.studenti = studenti
        self.id = id
        
        btnOk = QtWidgets.QPushButton("Ukloni")
        btnOk.clicked.connect(self.ukloni_studenta)
        
        group = QtWidgets.QDialogButtonBox()
        group.addButton(btnOk, QtWidgets.QDialogButtonBox.AcceptRole)
        
        formLayout.addRow(group)
        
        self.setLayout(formLayout)
        
    def ukloni_studenta(self):
        self.studenti.delete_one(self.id)
        self.studenti.load_data()
        




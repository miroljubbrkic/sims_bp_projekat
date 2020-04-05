from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler

class StudentModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.students = FileHandler("student_data", "student_metadata.json")

    def get_element(self, index):
        return self.students.get_all()[index.row()]

    # metode za redefisanje read-only modela
    def rowCount(self, index):
        # return len(self.students)
        return len(self.students.get_all())

    def columnCount(self, index):
        return 2 # zbog broja atributa koje prikazujemo o studentu

    def data(self, index, role=QtCore.Qt.DisplayRole):
        student = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return student.broj_indeksa
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return student.ime_prezime

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj indeksa"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime i prezime"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        student = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole: #broj indeksa
            student.broj_indeksa = value
            self.students.edit(index, student) # ovo je proba edita !!!!!!!!!!!!!
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole: #broj indeksa
            student.ime_prezime = value
            self.students.edit(index, student) # ovo je proba edita !!!!!!!!!!!!!
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable #ili nad bitovima
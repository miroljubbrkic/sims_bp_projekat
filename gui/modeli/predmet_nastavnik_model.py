from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler

class PredmetNastavnikModel(QtCore.QAbstractTableModel):
    def __init__(self, predmeti, parent=None):
        super().__init__(parent)
        self.nastavnici = []
        self.predmeti = predmeti

    def get_element(self, index):
        return self.nastavnici[index.row()]

    def rowCount(self, index):
        return len(self.nastavnici)

    def columnCount(self, index):
        return 4

    def data(self, index, role=QtCore.Qt.DisplayRole):
        nastavnik = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return nastavnik.ime
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return nastavnik.prezime
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return nastavnik.datum_rodjenja
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return nastavnik.tip


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        # section u zavisnosti od orijentacije je red ili kolona
        # orijentacija je vertikalna ili horizontalna
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Prezime"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Datum rodjenja"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "tip"

    # ove metode definisu editabilni model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        nastavnik = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole: 
            nastavnik.ime = value
            self.predmeti.edit(index, nastavnik)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole: 
            nastavnik.prezime = value
            self.predmeti.edit(index, nastavnik)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole: 
            nastavnik.datum_rodjenja = value
            self.predmeti.edit(index, nastavnik)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole: 
            nastavnik.tip = value
            self.predmeti.edit(index, nastavnik)
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable 
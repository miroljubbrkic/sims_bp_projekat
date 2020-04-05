from PySide2 import QtWidgets, QtCore


class NepolozeniPredmetModel(QtCore.QAbstractTableModel):
    def __init__(self,studenti, parent=None):
        super().__init__(parent)
        self.nepolozeni_predmeti = [] 
        self.studenti = studenti


    def get_element(self, index):
        return self.nepolozeni_predmeti[index.row()]


    def rowCount(self, index):
        return len(self.nepolozeni_predmeti)

    def columnCount(self, index):
        return 3 

    def data(self, index, role=QtCore.Qt.DisplayRole):
        nepolozeni_predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return nepolozeni_predmet.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return nepolozeni_predmet.silabus
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return nepolozeni_predmet.broj_pokusaja


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Silabus"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj pokušaja"

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        nepolozeni_predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            nepolozeni_predmet.naziv = value
            self.studenti.edit(index, nepolozeni_predmet)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole: 
            nepolozeni_predmet.silabus = value
            self.studenti.edit(index, nepolozeni_predmet)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole: 
            nepolozeni_predmet.broj_pokusaja = value
            self.studenti.edit(index, nepolozeni_predmet)
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable 
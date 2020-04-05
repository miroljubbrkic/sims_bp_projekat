from PySide2 import QtWidgets, QtCore
from database.file_handler import FileHandler

class PredmetModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.predmeti = FileHandler("predmet_data", "predmet_metadata.json")

    def get_element(self, index):
        # vratiti studenta na datom redu
        return self.predmeti.get_all()[index.row()]

    def rowCount(self, index):
        return len(self.predmeti.get_all())

    def columnCount(self, index):
        return 4 

    def data(self, index, role=QtCore.Qt.DisplayRole):
        predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return predmet.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return predmet.silabus
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return predmet.broj_casova_nedeljno
        elif index.column() == 3 and role == QtCore.Qt.DisplayRole:
            return predmet.broj_semestra


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Silabus"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj casova nedeljno"
        elif section == 3 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj semestra"

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            predmet.naziv = value
            self.predmeti.edit(index, predmet)
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            predmet.silabus = value
            self.predmeti.edit(index, predmet)
            return True
        elif index.column() == 2 and role == QtCore.Qt.EditRole: 
            predmet.broj_casova_nedeljno = value
            self.predmeti.edit(index, predmet)
            return True
        elif index.column() == 3 and role == QtCore.Qt.EditRole:
            predmet.broj_semestra = value
            self.predmeti.edit(index, predmet)
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable
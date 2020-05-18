from PySide2 import QtWidgets, QtCore
from gui.form import Form

class Model(QtCore.QAbstractTableModel):
    def __init__(self, data_list, parent=None):
        super().__init__(parent)
        self.data_list = data_list

    def get_element(self, index):
        return self.data_list.get_all()[index.row()]

    def rowCount(self, index):
        return len(self.data_list.get_all())

    def columnCount(self, index):
        return len(self.data_list.metadata["collumns"])

    def data(self, index, role=QtCore.Qt.DisplayRole):
        selected_data = self.get_element(index)
        for i in range(len(self.data_list.metadata["collumns"])):
            if index.column() == i and role == QtCore.Qt.DisplayRole:
                return getattr(selected_data, self.data_list.metadata["collumns"][i])

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        for i in range(len(self.data_list.metadata["collumns"])):
            if section == i and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole: # dodati proveru ako je collumns tipa list nemoj ga kreirati !!!!!
                return self.data_list.metadata["collumns"][i].replace("_"," ").capitalize()

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        selected_data = self.get_element(index)
        temp_data = selected_data
        if value == "":
            return False
        for i in range(len(self.data_list.metadata["collumns"])):
            if index.column() == i and role == QtCore.Qt.EditRole:
                setattr(temp_data, self.data_list.metadata["collumns"][i], value)
                self.data_list.edit(selected_data, temp_data)
                return True
        return False

    def removeRows(self, row, rows, index=QtCore.QModelIndex()):
        selected_data = self.get_element(index)
        self.beginRemoveRows(QtCore.QModelIndex(), row, row + rows - 1)
        self.data_list.delete_one(self.get_element(index))
        self.endRemoveRows()
        return True

    def insertRows(self, row, rows, index=QtCore.QModelIndex()):
        self.beginInsertRows(QtCore.QModelIndex(), row, row + rows-1)
        forma = Form(self.data_list)
        obj = forma.get_object()
        if obj is None:
            return False
        self.data_list.insert(obj)
        self.endInsertRows()
        return True



    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable




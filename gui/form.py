from PySide2 import QtWidgets, QtCore ,QtGui
from database.klase.student import Student
from database.klase.nastavnik import Nastavnik
from database.klase.predmet import Predmet


class Form(QtWidgets.QDialog):
    def __init__(self, data_type, parent=None):
        super(Form, self).__init__(parent)
        self.data_type = data_type

        self.setWindowTitle("Dodavanje " + data_type.metadata["class"].lower() + "a")
        self.setWindowIcon(QtGui.QIcon("icons/angry.ico"))
        self.formGroupBox = QtWidgets.QGroupBox("Dodavanje " + data_type.metadata["class"].lower() + "a")
        self.layout = QtWidgets.QFormLayout()
        self.dodaj = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok)

        self.lista = []

        for i in range(len(data_type.metadata["collumns"])):
            self.line_edit = QtWidgets.QLineEdit()
            self.line_edit.setFixedSize(200,40)
            self.layout.addRow(QtWidgets.QLabel(data_type.metadata["collumns"][i].replace("_"," ")+ ": "),self.line_edit)
            
            self.lista.append(self.line_edit)

        

        self.setLayout(self.layout)
        self.layout.addWidget(self.dodaj)


        def find_class(self):
            if self.data_type.metadata["class"] == "Student":
                print("Izabran je student")
                rand_lista = ["qwerty","12345"]
                s = Student()
                for i in range(len(self.data_type.metadata["collumns"])):
                    setattr(s, self.data_type.metadata["collumns"][i], rand_lista[i])
                
                print(s.broj_indeksa,s.ime_prezime)
            
            if self.data_type.metadata["class"] == "Nastavnik":
                print("Izabran je nastavnik")
                # Nastavnik("","","","","")

            if self.data_type.metadata["class"] == "Predmet":
                print("Izabran je predmet")
                # Predmet("","","","","",[])

        find_class(self)
        self.display()

    def display(self):
        self.exec_()

    def provera(self):
        pass
    #! dodati da ne dozvoljava da su polja prazna
    

    

    






import sys
from PySide2 import QtWidgets, QtGui, QtCore
from gui.student_widget import StudentWidget
from gui.predmet_widget import PredmetWidget
from gui.nastavnik_widget import NastavnikWidget



if __name__ == "__main__":

    def file_clicked(index):
        print(file_system_model.filePath(index))

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_window.resize(800, 500)
    main_window.setWindowTitle("Editor generickih podataka")
    main_window.setWindowIcon(QtGui.QIcon("icons8-edit-file-64.png"))

    menu_bar = QtWidgets.QMenuBar(main_window)
    file_menu = QtWidgets.QMenu("File", menu_bar)
    edit_menu = QtWidgets.QMenu("Edit", menu_bar)
    view_menu = QtWidgets.QMenu("View", menu_bar)
    help_menu = QtWidgets.QMenu("Help", menu_bar)

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(view_menu)
    menu_bar.addMenu(help_menu)

    tool_bar = QtWidgets.QToolBar(main_window)

    central_widget = QtWidgets.QTabWidget(main_window)
    student_workspace = StudentWidget(central_widget)
    central_widget.addTab(student_workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Studenti")

    
    predmet_workspace = PredmetWidget(central_widget)
    central_widget.addTab(predmet_workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Predmeti")
    
    nastavnik_workspace = NastavnikWidget(central_widget)
    central_widget.addTab(nastavnik_workspace, QtGui.QIcon("icons8-edit-file-64.png"), "Nastavnici")
    
    structure_dock = QtWidgets.QDockWidget("Structure dock", main_window)

    file_system_model = QtWidgets.QFileSystemModel()
    file_system_model.setRootPath(QtCore.QDir.currentPath())

    tree_view = QtWidgets.QTreeView()
    tree_view.setModel(file_system_model)

    tree_view.setRootIndex(file_system_model.index(QtCore.QDir.currentPath() + "/database/data"))

    structure_dock.setWidget(tree_view)

    toggle_structure_dock_action = structure_dock.toggleViewAction()
    view_menu.addAction(toggle_structure_dock_action)

    tree_view.clicked.connect(file_clicked)

    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar je prikazan!")

    
    main_window.setMenuBar(menu_bar)
    main_window.addToolBar(tool_bar)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, structure_dock)
    main_window.setCentralWidget(central_widget)
    main_window.setStatusBar(status_bar)
    main_window.show()
    sys.exit(app.exec_())

    


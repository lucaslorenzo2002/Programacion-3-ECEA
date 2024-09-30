from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from business.cuilLogic import cuilCalculator
from presentation.MainWindow import Ui_MainWindow
from presentation.Dialogo import Ui_Dialog
from business.export import Export
from os import getcwd

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.cmbGenero.addItem('Masculino', 'M')
        self.cmbGenero.addItem('Femenino', 'F')

        self.btnGenerar.clicked.connect(self.Generar)
        self.actionExport.triggered.connect(self.Ejecutar)

    def Ejecutar(self):
        dialog = MyDialog(self)  
        result = dialog.exec() 
        if result == 0:
            self.statusbar.showMessage("Exportacion cancelada", 5000)
        if result == 1 :
            data = {'genero': self.cmbGenero.currentData(), 'dni': self.cmbDni.text(), 'cuil': self.cmbCuil.text()}
            result = Export(data).exportFile()
            self.statusbar.showMessage("Exportacion exitosa", 5000)



    def Generar(self):
        genero = self.cmbGenero.currentData()
        dni = self.cmbDni.text()
        myCuil = cuilCalculator(dni, genre=genero)

        try:
            myCuil.validate()
            result = myCuil.calculate()
            self.cmbCuil.setText(result)
        except Exception as e:
            self.cmbCuil.setText(e.args[0])

class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
        route = getcwd() + '\Cuil.txt'
        self.lineEditRoute.setText(route)
        self.btnAceptar.clicked.connect(lambda: self.done(1))
        self.pushButton_2.clicked.connect(lambda: self.close())

app = QApplication([])

window = MyMainWindow()
window.show()

app.exec()

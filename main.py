from PyQt6.QtWidgets import QApplication, QMainWindow
from presentation.program import Ui_Dialog
from business.cuilLogic import cuilCalculator

class MyDialog(QMainWindow, Ui_Dialog):
    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

        self.cmbGenero.addItem('Masculino', 'M')
        self.cmbGenero.addItem('Femenino', 'F')

        self.btnGenerar.clicked.connect(self.Generar)


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

app = QApplication([])
window = MyDialog()
window.show()
app.exec()
# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 356)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 49, 16))
        self.label_2.setObjectName("label_2")
        self.cmbGenero = QtWidgets.QComboBox(parent=Dialog)
        self.cmbGenero.setGeometry(QtCore.QRect(40, 40, 111, 22))
        self.cmbGenero.setObjectName("cmbGenero")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 49, 16))
        self.label_3.setObjectName("label_3")
        self.cmbDni = QtWidgets.QLineEdit(parent=Dialog)
        self.cmbDni.setGeometry(QtCore.QRect(40, 130, 113, 21))
        self.cmbDni.setObjectName("cmbDni")
        self.cmbCuil = QtWidgets.QLineEdit(parent=Dialog)
        self.cmbCuil.setGeometry(QtCore.QRect(40, 220, 113, 21))
        self.cmbCuil.setObjectName("cmbCuil")
        self.btnGenerar = QtWidgets.QPushButton(parent=Dialog)
        self.btnGenerar.setGeometry(QtCore.QRect(40, 290, 231, 24))
        self.btnGenerar.setObjectName("btnGenerar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "GENERO"))
        self.label_2.setText(_translate("Dialog", "DNI"))
        self.label_3.setText(_translate("Dialog", "CUIL"))
        self.btnGenerar.setText(_translate("Dialog", "Generar"))
